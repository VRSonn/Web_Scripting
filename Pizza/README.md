Pizza Pizzazz Application

I've created an HTML page and CGI Perl script that enables ordering a pizza from Pizza Pizzazz.

The HTML Page

    The form uses radio buttons for selecting a size and checkboxes for optional toppings.
    Sizes for plain pizza are regular $6.00, large $8.00, and family $11.00. Toppings are $1.25 each.
    Textboxes enable a customer to enter a name, phone number and address for delivery.

The CGI Script

    Created a hash of pizza sizes and associated prices.
    The customer's size selection enables reading the price of a plain pizza from this hash.
    The toppings are stored in an array.
    The toppings are used to complete the pricing of the pizza.
    The script displays an itemized summary of the order and the total due on delivery.
    Delivery information is shown by the script.
