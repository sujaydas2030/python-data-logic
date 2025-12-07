"""
Extracts email username and domain.
"""
# Taking the input
import string
text = input()

def extract_email_data(text):
    # Write your code here
  emails=[]
  text_list=text.split()
  for texts in text_list:
    if '@' in texts:
      # Strip common punctuation like commas and quotes from the ends
      cleaned_email = texts.strip(string.punctuation)
      emails.append(cleaned_email)
  final_lst=[]
  for email in emails:
    indx=email.index('@')
    username=email[:indx]
    domain=email[indx+1:]
    final_lst.append((username,domain))
  return final_lst

# Print the output
print(extract_email_data(text))
