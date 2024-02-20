email_id_by_user = input("Enter the email id to be sliced : ").strip()
email_name_part = email_id_by_user[:email_id_by_user.index("@")]
email_domain_part = email_id_by_user[email_id_by_user.index("@")+1:]
print(f"the name part of the email id is {email_name_part} and the domain part is {email_domain_part}.")
