# Replace each occurrence of some number by the actual number surrounded by the
# number as a string. That prevents messing up other numbers. Since it
# eventually takes the first and last number I won't care about the garbage
# generated in between
cat $1 | sed 's/one/one1one/g' \
       | sed 's/two/two2two/g' \
       | sed 's/three/three3three/g' \
       | sed 's/four/four4four/g' \
       | sed 's/five/five5five/g' \
       | sed 's/six/six6six/g' \
       | sed 's/seven/seven7seven/g' \
       | sed 's/eight/eight8eight/g' \
       | sed 's/nine/nine9nine/g' \
       | sed 's/[^0-9]*//g' | sed 's/\(.*\)/\1\1/g' | sed 's/\([0-9]\).*\([0-9]\)/\1\2/g' | paste -sd+ - | bc
