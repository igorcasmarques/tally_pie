from config import copy, messages
from widgets import buttons


def update_pie_chart(app):
    """Update the pie chart each time a wedge's size changes."""
    calculate_total_count(app)
    calculate_wedge_percentages(app)
    draw_pie_chart(app)
    buttons.update_main_button(app)

def calculate_total_count(app):
    """Update the total count of the pie chart."""
    app.total_count = sum(wedge.size for wedge in app.wedges)
    app.total_count_label.config(text=f"{copy.total_count} {app.total_count}")

def calculate_wedge_percentages(app):
    """Update the size percentages of all wedges."""
    if app.total_count != 0:
        for wedge in app.wedges:
            wedge.percentage = 100 * (wedge.size / app.total_count)

def draw_pie_chart(app):
    """Redraw the pie chart each time a wedge's size changes."""
    pie_chart = app.pie_chart
    title = pie_chart.title
    pie_chart_labels = []
    pie_chart_sizes = []
    
    # Reset pie chart
    if app.total_count == 0:
        draw_empty_pie(app, pie_title=title)
        return

    # Redraw pie chart
    for wedge in app.wedges:
        if wedge.size != 0:
            pie_chart_labels.append(wedge.name)
            pie_chart_sizes.append(wedge.percentage)

    pie_chart.ax.clear()

    if app.wedges:
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
    """Clear all wedges of an existing pie chart."""
    wedges = app.wedges
    if wedges:
        for wedge in wedges:
            wedge.frame.destroy()
        wedges.clear()
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