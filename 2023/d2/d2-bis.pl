#### Strict and warnings

use strict;
use warnings;

use List::Util qw(max);

# For reading:
open(my $in,  "<",  "$ARGV[0]")  or die "Can't open sample.txt: $!";

my $power_sum = 0;

while (my $line = <$in>) {
  my @matches_red = $line =~ m/(\d+) red/g;
  my @matches_green = $line =~ m/(\d+) green/g;
  my @matches_blue = $line =~ m/(\d+) blue/g;
  my $power = (max @matches_red) * (max @matches_green) * (max @matches_blue);
  $power_sum += $power;
}

print "TOTAL POWER SUM: $power_sum\n";
