# First removes all non numeric characters, then we duplicate each row so we
# can get via regexp the first and last characters and only keep those (the
# duplication is because there might be lines with a single number). Lastly,
# pipe the results into bc
cat $1 | sed 's/[^0-9]*//g' | sed 's/\(.*\)/\1\1/g' | sed 's/\([0-9]\).*\([0-9]\)/\1\2/g' | paste -sd+ - | bc
