from config import copy, messages
from widgets import buttons


def update_pie_chart(app):
    """Update the pie chart each time a category is tallied up or down."""
    calculate_total_tally(app)
    calculate_tally_percentages(app)
    draw_pie_chart(app)
    buttons.update_main_button(app)

def calculate_total_tally(app):
    """Update the total tally of the app."""
    app.total_tally = sum(cat.tally for cat in app.cats)
    app.total_tally_label.config(text=f"{copy.total_tally} {app.total_tally}")

def calculate_tally_percentages(app):
    """Update the tally percentages of all category."""
    if app.total_tally != 0:
        for cat in app.cats:
            cat.tally_percent = 100 * (cat.tally / app.total_tally)

def draw_pie_chart(app):
    """Redraw the pie chart each time a category is tallied up or down."""
    pie_chart = app.pie_chart
    title = pie_chart.title
    pie_chart_labels = []
    pie_chart_sizes = []
    
    # Reset pie chart
    if app.total_tally == 0:
        draw_empty_pie(app, pie_title=title)
        return

    # Redraw pie chart
    for cat in app.cats:
        if cat.tally != 0:
            pie_chart_labels.append(cat.cat_name)
            pie_chart_sizes.append(cat.tally_percent)

    pie_chart.ax.clear()

    if app.cats:
        pie_chart.ax.pie(
            pie_chart_sizes, 
            labels=pie_chart_labels, 
            autopct=lambda pct: dynamic_autopct(pct, pie_chart.sizes), 
            startangle=90)
    else:
        pie_chart.ax.pie(pie_chart.sizes, labels=pie_chart.labels, autopct='', startangle=90)
    
    pie_chart.ax.axis('equal')
    pie_chart.ax.set_title(title)
    pie_chart.canvas.draw()

def dynamic_autopct(pct, sizes):
    """Establish how percentages are displayed in the pie chart."""
    if pct > 10:
        if int(pct * 10) % 10 == 0:
            return '%d%%' % pct
        else:
            return '%1.1f%%' % pct
    elif pct < 4:
        return ''
    else:
        return '%d%%' % pct

def change_title(master, app, name, window, event=None):
    """Change the title of a pie chart."""
    new_pie_name = name.get()
    if new_pie_name != "":      
        pie_chart = app.pie_chart
        pie_chart.title = new_pie_name
        pie_chart.ax.set_title(new_pie_name)
        pie_chart.canvas.draw()
        window.destroy()

    else:
        messages.warning_box('empty_pie')
        name.focus()

def reset_pie(app, pie_title=''):
    """Clear all categories of an existing pie chart."""
    cats = app.cats
    if cats:
        for cat in cats:
            cat.frame.destroy()
        cats.clear()
    draw_empty_pie(app, pie_title)

def draw_empty_pie(app, pie_title='', autopct=''):
    """Draw an empty pie chart."""
    pie_chart = app.pie_chart

    pie_chart.ax.clear()
    pie_chart.title = pie_title
    pie_chart.ax.set_title(pie_chart.title)
    pie_chart.ax.pie(pie_chart.sizes, labels=pie_chart.labels, autopct=autopct, startangle=90)
    pie_chart.ax.axis('equal')
    pie_chart.canvas.draw()