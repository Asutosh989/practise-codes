s = input()
x = int(input())
y = list(input().strip().split())

def get_all_substrings(string):
   length = len(string)+1
   return [string[x:y] for x in range(length) for y in range(length) if string[x:y]]

sub = get_all_substrings(s)
sub = set(sub)
