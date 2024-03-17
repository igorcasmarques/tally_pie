# Tally Pie

## Introduction

This guide will show you how to install and use Tally Pie on your computer. These tasks are accessible to people of any technical background and can be done in a few minutes.

This introductory section contains information about the following topics:

- [What is Tally Pie?](#what-is-tally-pie)
- [Requirements](#requirements)
- [Contribute](#contribute)
- [Guide conventions](#guide-conventions)
- [Organization of the guide](#organization-of-the-guide)

### What is Tally Pie?

**Developed by**: [Mudpuppy (Ottawa, Canada)](www.igormarques.ca)  
**Current version**: 0.1.0 (Alpha)

Tally Pie is an [open-source](LICENSE.md) desktop app for counting and categorizing content with a dynamic pie chart. You can create pie charts with up to six wedges very quickly with Tally Pie's simple user interface (UI). As you increment or decrement wedges, the pie chart changes in real-time to reflect the evolving sizes of wedges.

Tally Pie is great for conducting quick ad hoc surveys, like:

- Keeping score in party games
- Doing a quick opinion poll with friends
- Counting household objects
- Categorizing content on social media

### Requirements

You can run Tally Pie as a Python package or as a standalone executable, i.e., from a single file. To run Tally Pie as a Python package, you first need to install [Git](https://git-scm.com/downloads) and [Python](https://www.python.org/downloads/); Tally Pie currently supports Python 3.8 to 3.12.  

The table below shows the operating systems (OS) supported by Tally Pie's package and executable:

| OS                     | Python package     | Standalone executable |
|------------------------|:------------------:|:---------------------:|
| Windows 10 and 11      | :white_check_mark: | :white_check_mark:    |
| macOS Mojave and later | :white_check_mark: | :x:                   |  

### Contribute

You can contribute to Tally Pie. If you find any bugs or have suggestions for features or improvements, please [open an issue](https://github.com/igorcasmarques/tally_pie/issues).

### Guide conventions

This guide relies on the following visual conventions:

> :book: **Notes** tell you how to perform a procedure in a different and often easier way.

> :warning: **Warnings** draw attention to something you should do to avoid issues when you perform a procedure. 

```
Code excerpts show you what to type in the command-line interface (CLI).
```

### Organization of this guide

The table below details the content of the following four sections of this guide:

| Section | Purpose |
|---------|---------|
|[Overview of the UI](#overview-of-the-ui) | Introduce you to Tally Pie's UI with an annotated screenshot |
|[Starting up Tally Pie](#starting-up-tally-pie)| Show you how to get Tally Pie as a Python package or as a standalone executable |
|[Using Tally Pie](#using-tally-pie)| Show you how to use all of Tally Pie's features  |
|[Error and warning messages](#error-and-warning-messages)| Explain Tally Pie's warning and error messages and how to fix the issues they raise |

## Overview of the UI

<table>
  <tbody>
    <tr>
      <td width="300">
        <img src="https://tally-pie.s3.ca-central-1.amazonaws.com/readme-1.png" alt="Screenshot of Tally Pie's UI with six numbered labels" width="300" height ="auto">
      </td>
      <td>
        <ol>
          <li><b>Menu bar</b>: Has three menus (File, Edit, and Help) with the commands that enable you to create, edit, and erase pie charts.</li>
          <li><b>Total items count</b>: Displays the sum of the sizes of all wedges in the pie chart.</li>
          <li><b>Chart title</b>: Displays the title you give a pie chart when you create it. You can rename the pie chart and change this title at any time.
          <li><b>Pie chart area</b>: Displays the app's dynamic pie chart, which is updated each time you change the size of a wedge.</li>
          <li><b>Main button</b>: Has two functions: when there is no pie chart, it says <b>New Pie</b> and enables you to create a new pie chart; when there is a pie chart, it says <b>Add Wedge</b> and enables you to add a new wedge to the pie chart.</li>
          <li><b>Wedge label</b>: Displays a wedge's name and size and has three buttons: increment the wedge, decrement the wedge, and remove the wedge.</li>
        </ol>
      </td>
    </tr>
  </tbody>
</table>

## Starting up Tally Pie

This section will show you how to get Tally Pie, which you can get as a package or as an executable. Both versions have the exact same app but you may choose one over the other depending on the following factors:

| Version               | Coding required? | OS support     | Size   |
|-----------------------|------------------|----------------|--------|
| Python package        | Yes              | Windows, macOS | 856 KB |
| Standalone executable | No               | Windows        | 128 MB |

This section has two topics:

- [Running Tally Pie as a Python package](#running-tally-pie-as-a-python-package)
- [Running Tally Pie as a standalone executable](#running-tally-pie-as-a-standalone-executable)

### Running Tally Pie as a Python package

If you are comfortable working with Python, you can run Tally Pie as a package after cloning its repository and installing its dependencies. The package is much lighter than the executable and gives you more control over the program's source code, allowing you to customize it. If you don't want to deal with coding, skip ahead to learn how to run Tally Pie as a [standalone executable](#running-tally-pie-as-a-standalone-executable).

This topic will show you how:

- [To install the Python package](#to-install-the-python-package)
- [To run the Python package](#to-run-the-python-package)

#### To install the Python package

1. In the CLI, navigate to the directory you want Tally Pie to be in.
1. Clone Tally Pie's repository:
```
git clone https://github.com/igorcasmarques/tally_pie.git
```
3. Install the package's required dependencies:
```
pip install -r requirements.txt
```

#### To run the Python package

- In the CLI, run the app:
```
python app.py
```

### Running Tally Pie as a standalone executable

The easiest way to use Tally Pie is to run it as a standalone executable. It takes up more storage space than the package and will not give you access to the source code, but if these things do not inconvenience you, all you have to do is download a single file, open it, and start using Tally Pie right away.

> :warning: The Tally Pie executable does not currently support macOS. It will probably run well with [Wine](https://www.winehq.org), but this has not been tested. If you have macOS, prefer to run Tally Pie as [a Python package](#running-tally-pie-as-a-python-package).

This topic will show you how:

- [To download the standalone executable](#to-download-the-standalone-executable)
- [To run the standalone executable](#to-run-the-standalone-executable)

#### To download the standalone executable

- Download [**tally_pie.zip**](https://drive.google.com/uc?export=download&id=1jwn2KHvizJbU8uH_t1y8ghJ0OgRj8w6i)

#### To run the standalone executable

1. Extract **tally_pie.zip**.
1. In the extracted folder, double-click **tally_pie.exe**.

## Using Tally Pie

This section will show you how to use Tally Pie to create pie charts, add wedges, change the sizes of wedges, and save your work. Because of Tally Pie's intuitive UI, you can start surveying things within seconds of opening the app.

This section has three topics:

- [Managing pie charts](#managing-pie-charts)
- [Managing wedges](#managing-wedges)
- [Managing pie chart files](#managing-pie-chart-files)

### Managing pie charts

Tally Pie enables you to create and edit pie charts so you can count and categorize things visually. Pie charts are graphs that illustrate mathematical proportions using wedges on a circle. Many people like pie charts because they make it easy to see how the size of a wedge relates to the other wedges and to the pie as a whole.

This topic will show you how:

- [To create a pie chart](#to-create-a-pie-chart)
- [To rename a pie chart](#to-rename-a-pie-chart)
- [To erase a pie chart](#to-erase-a-pie-chart)

#### To create a pie chart

1.	Select **File > New**.
2.	On the dialogue box, enter a title for your new pie chart.
3.	Select **Create pie**.

<img src="https://tally-pie.s3.ca-central-1.amazonaws.com/readme-2.png" alt="Screenshot of Tally Pie's UI with the File menu expanded, the New menu item highlighted, and the pie chart creation dialogue box open" width="200" height ="auto">

> :book: You can also press Ctrl+N or select **New Pie** on the bottom of the window to create a new pie chart.

#### To rename a pie chart

1.	Select **Edit > Rename pie**.
2.	On the dialogue box, enter a new title for your pie chart.
3.	Select **Rename pie**.

<img src="https://tally-pie.s3.ca-central-1.amazonaws.com/readme-3.png" alt="Screenshot of Tally Pie's UI with the Edit menu expanded, the Rename pie menu item highlighted, and the pie chart renaming dialogue box open" width="200" height ="auto">

> :book: You can also press Ctrl+R to rename a new pie chart.

#### To erase a pie chart

1.	Select **Edit > Erase pie**.
2.	On the confirmation dialogue box, select **Yes**.

<img src="https://tally-pie.s3.ca-central-1.amazonaws.com/readme-4.png" alt="Screenshot of Tally Pie's UI with the Edit menu expanded, the Erase pie menu item highlighted, and the confirmation dialogue box open" width="200" height ="auto">

> :book: You can also press Ctrl+W to erase a new pie chart.

### Managing wedges

After creating and naming your pie chart, you need to add wedges to it. Each time you increment or decrement a wedge, the pie chart changes to reflect the new proportions between wedges. Since the usefulness of a pie chart decreases the more wedges it has, you can only add up to six wedges in Tally Pie.

This topic will show you how:

- [To add a wedge](#to-add-a-wedge)
- [To increment a wedge](#to-increment-a-wedge)
- [To decrement a wedge](#to-decrement-a-wedge)
- [To remove a wedge](#to-remove-a-wedge)

#### To add a wedge

1.	Select **Edit > Add wedge**.
2.	On the dialogue box, enter a name for your new wedge.
3.	Select **Add wedge**.

<img src="https://tally-pie.s3.ca-central-1.amazonaws.com/readme-5.png" alt="Screenshot of Tally Pie's UI with the Edit menu expanded, the Add wedge menu item highlighted, and the wedge creation dialogue box open." width="200" height ="auto">

> :book: You can also press Ctrl+L or select **Add Wedge** below the pie chart to add a wedge.

#### To increment a wedge

- Select **+1** on the wedge’s label.

<img src="https://tally-pie.s3.ca-central-1.amazonaws.com/readme-6.png" alt="Screenshot of Tally Pie's UI with the a red circle around the +1 button on a wedge labe." width="200" height ="auto">

#### To decrement a wedge

- Select **-1** on the wedge’s label.

<img src="https://tally-pie.s3.ca-central-1.amazonaws.com/readme-7.png" alt="Screenshot of Tally Pie's UI with the a red circle around the +1 button on a wedge label." width="200" height ="auto">

#### To remove a wedge

- Select **x** on the wedge’s label.

<img src="https://tally-pie.s3.ca-central-1.amazonaws.com/readme-8.png" alt="Screenshot of Tally Pie's UI with the a red circle around the +1 button on a wedge labe." width="200" height ="auto">

### Managing pie chart files

Tally Pie is best suited for quick one-time surveys. However, if your project takes longer than a single session or if you want to share your pie chart with others, Tally Pie enables you to save your work as JSON files.

This topic will show you how:

- [To save a pie chart](#to-save-a-pie-chart)
- [To open a pie chart](#to-open-a-pie-chart)

#### To save a pie chart

1.	Select **File > Save**.
2.	On the dialogue box, navigate to your desired folder.
3.	Enter a name for your pie chart file.
4.	Select **Save**.

<img src="https://tally-pie.s3.ca-central-1.amazonaws.com/readme-9.png" alt="Screenshot of Tally Pie's UI with the File menu expanded and the Save menu item highlighted." width="200" height ="auto">

> :book: You can also press Ctrl+S to save a pie chart.

#### To open a pie chart

1.	Select **File > Open**.
2.	On the dialogue box, locate the JSON file with your pie chart.
3.	Select **Open**.

<img src="https://tally-pie.s3.ca-central-1.amazonaws.com/readme-10.png" alt="Screenshot of Tally Pie's UI with the File menu expanded and the Save menu item highlighted." width="200" height ="auto">

> :book: You can also press Ctrl+O to open a pie chart.
 
## Error and warning messages

This section contains a list of error and warning messages you may encounter while using Tally Pie, their causes, and what you can do to solve the issues they raise. 

<table>
  <tbody>
    <tr>
      <th>Message</th>
      <th>Type</th>
      <th>Cause</th>
      <th>Solution</th>
    </tr>  
    <tr>
      <td width="200">
        <img src="https://tally-pie.s3.ca-central-1.amazonaws.com/readme-11.png" alt="Screenshot of a warning message that says, This pie chart needs a title." width="200" height ="auto">
      </td>
      <td>:warning: Warning</td>
      <td>You tried creating a pie chart but forgot to give it a title.</td>
      <td>Enter a title for your pie chart and select <b>Create pie chart</b>.</td>
    </tr>
    <tr>
      <td width="200">
        <img src="https://tally-pie.s3.ca-central-1.amazonaws.com/readme-12.png" alt="Screenshot of a warning message that says, This wedge needs a name." width="200" height ="auto">
      </td>
      <td>:warning: Warning</td>
      <td>You tried creating a wedge but forgot to give it a name.</td>
      <td>Enter a name for your wedge and select <b>Add wedge</b>.</td>
    </tr>
    <tr>
      <td width="200">
        <img src="https://tally-pie.s3.ca-central-1.amazonaws.com/readme-13.png" alt="Screenshot of a warning message that says, This name cannot exceed 25 characters." width="200" height ="auto">
      </td>
      <td>:warning: Warning</td>
      <td>You tried giving a pie chart or a wedge a very long name.</td>
      <td>Keep the names of your pie charts or wedges under 26 characters.</td>
    </tr>
    <tr>
      <td width="200">
        <img src="https://tally-pie.s3.ca-central-1.amazonaws.com/readme-14.png" alt="Screenshot of a warning message that says, This name is taken by another wedge." width="200" height ="auto">
      </td>
      <td>:warning: Warning</td>
      <td>You tried giving two wedges the same name.</td>
      <td>Give unique names to each of your pie chart's wedges.</td>
    </tr>
    <tr>
      <td width="200">
        <img src="https://tally-pie.s3.ca-central-1.amazonaws.com/readme-15.png" alt="Screenshot of a warning message that says, You can only add up to six wedges." width="200" height ="auto">
      </td>
      <td>:warning: Warning</td>
      <td>You tried creating more than six wedges.</td>
      <td>If you need more than six wedges, use a bar graph in another app instead.</td>
    </tr>
    <tr>
      <td width="200">
        <img src="https://tally-pie.s3.ca-central-1.amazonaws.com/readme-16.png" alt="Screenshot of a warning message that says, There is no data to save yet." width="200" height ="auto">
      </td>
      <td>:warning: Warning</td>
      <td>You tried saving an empty pie chart.</td>
      <td>Add content to your pie chart before saving it.</td>
    </tr>
    <tr>
      <td width="200">
        <img src="https://tally-pie.s3.ca-central-1.amazonaws.com/readme-17.png" alt="Screenshot of a warning message that says, File not found." width="200" height ="auto">
      </td>
      <td>:no_entry: Error</td>
      <td>You tried opening a file that does not exist.</td>
      <td>Double check the file's location before trying to open it.</td>
    </tr>
    <tr>
      <td width="200">
        <img src="https://tally-pie.s3.ca-central-1.amazonaws.com/readme-18.png" alt="Screenshot of a warning message that says, File not found." width="150" height ="auto">
      </td>
      <td>:no_entry: Error</td>
      <td>You tried opening an invalid JSON file that cannot be transformed into a pie chart by Tally Pie.</td>
      <td>Choose a different JSON file or create a new pie chart.</td>
    </tr>
  </tbody>
</table>

