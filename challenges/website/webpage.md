
# Display data as a HTML page

In this exercise you will display a table on a HTML-page by starting your own web server with `bottle`.

**Warning:** This exercise assumes you have basic knowledge on web servers and HTML pages. If you have never created a web page, it is probably easier to try the **DjangoGirls Tutorial** (which is much better documented).

## 1. Launch Bottle

Start a hello world web server using Bottle.

## 2. Add a template

Create a file `views/template_name.tpl` (a HTML file).
Add a template to the bottle server and connect it to the Python script by:

    @view('template_name')


## 3. Supply variables

Fill the template with data from a variable by returning from the view:

    return {'text': ... }

Add a directive to the HTML template like:

    {{!text}}


## 4. Create headers and footers

Add a HTML header and footer to make the page nicer, include them in the template:

    % include('header.tpl')

## 5. Data from CSV

Supply data to the form results from the CSV file `grosse_laender_2015.csv`.

## 6. Forms

Create a form where the user can enter a parameter. Use `form.py` as a starting point.
