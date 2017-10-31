#!/usr/bin/perl -w

use strict;
use warnings;

use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
print "Content-type: text/html\n\n";


#create a hash to hold the pizza size and price
my %pizzaPrices = ('Regular' => '6',
					'Large' => '8',
					'Family' => '11');

#read/store the pizza size
my $pizzaSize = param('size');

#read/store the toppings in an array
my @toppings = param('toppings');
my $toppingPrice = 1.25;
#create a counter for the toppings
my $i = 0;

#read/store the delivery address
my $phone = param('phone');
my $name = param('name');
my $address = param('address');


print "<h2>Here is your Pizza Pizzaz Order: </h2>";

#display the selected pizza size and its price
printf "Size selected: $pizzaSize  \$%.2f", $pizzaPrices{$pizzaSize};

#display the toppings choosen and their price as an unordered list
print "<h4>Toppings selected</h4>";
print "<ul>";
foreach my $toppings(@toppings){
	printf "<li> $toppings \t \$%.2f",$toppingPrice;
	$i++;
}
print "</ul>";

#Calculate total for toppings
my $total = $pizzaPrices{$pizzaSize} + ($i * $toppingPrice);
printf "<h3>Total Due \$%.2f \t</h3>", $total;


#display address
print <<"HERE";
<h4>Delivery Information</h4>	
Name: $name</br>
Address: $address</br>
Telephone: $phone 
<h1>Enjoy Your Pizza</h1>
HERE
