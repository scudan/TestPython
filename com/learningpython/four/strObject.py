S = 'Spam'
print(len(S));
print(S[1]);
print(S[-2]);
#
#[i:j] => [i,j);
#

print(S[1:3])
print(S[:2])
print(S[:-1])
#Spamtest
print(S+'test');
#SpamSpamSpamSpam
print(S*4);


# is error
S[0] ='z'

# is right
S = 'z' + S[1:]


