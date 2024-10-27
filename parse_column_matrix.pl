use strict;
use warnings;

open(FH, "<", $ARGV[0]);
my @ans;
while(<FH>)
{
	chomp $_;
	push(@ans,$_);

}


open(RH2,">>",$ARGV[1]);

print RH2 "\n*\t";
print RH2 "@ans[0 .. 7]";#." 1.0 ".@ans2[35];
#print "\n\t\t";

print RH2 "\n*\t*\t";
print RH2 "@ans[8..14]";

#print "\n\t\t\t";

print RH2 "\n*\t*\t*\t";
print RH2 "@ans[15..20]";

#print "\n\t\t\t\t";

print RH2 "\n*\t*\t*\t*\t";
print RH2 "@ans[21..25]";

#print "\n\t\t\t\t\t";

print RH2 "\n*\t*\t*\t*\t*\t";
print RH2 "@ans[26..29]";

#print "\n\t\t\t\t\t\t";

print RH2 "\n*\t*\t*\t*\t*\t*\t";
print RH2 "@ans[30..32]";

#print "\n\t\t\t\t\t\t\t";

print RH2 "\n*\t*\t*\t*\t*\t*\t*\t";
print RH2 "@ans[33..34]";

#print "\n\t\t\t\t\t\t\t\t";

print RH2 "\n*\t*\t*\t*\t*\t*\t*\t*\t";
print RH2 "@ans[35]";
#print "\n";

print RH2 "\n*\t*\t*\t*\t*\t*\t*\t*\t*\t";
print RH2 "\n";
