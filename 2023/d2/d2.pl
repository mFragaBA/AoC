#### Strict and warnings

use strict;
use warnings;

use List::Util qw(any);

# For reading:
open(my $in,  "<",  "$ARGV[0]")  or die "Can't open sample.txt: $!";

my $valid_games = 0;
my $id_sum = 0;

while (my $line = <$in>) {
  $valid_games++;
  my @matches_red = $line =~ m/(\d+) red/g;
  my @matches_green = $line =~ m/(\d+) green/g;
  my @matches_blue = $line =~ m/(\d+) blue/g;
  if (any {$_ > 12} @matches_red or any {$_ > 13} @matches_green or any {$_ > 14} @matches_blue) {
    $valid_games--;
  } else {
    $line =~ /^Game (\d+)\:.*$/;
    my $game_id = $1;
    $id_sum += $game_id;
  }
}

print "VALID GAMES: $valid_games\n";
print "TOTAL ID SUM: $id_sum\n";
