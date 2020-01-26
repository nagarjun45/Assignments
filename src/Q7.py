def mail(email):
    formatEmail = email[email.find('@')+1:email.find('.')]
    return formatEmail

email = 'nagarjunr@gmail.com'
print(mail(email))