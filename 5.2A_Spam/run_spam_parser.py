import re
from email import message_from_string
from urllib.parse import urlparse

spam_email = '''From: cheap-deals@example.com
To: student@example.edu
Subject: Amazing deal - 90% OFF!
Date: Thu, 12 Nov 2025 09:15:00 -0500
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8

Hello!
Buy now and save 90% on our products. Visit http://cheap.example.com/deal to claim.
Unsubscribe: http://cheap.example.com/unsub
'''

phish_email = '''From: security-alert@banking.example.com
To: user@example.com
Subject: Action Required: Verify Your Account
Date: Fri, 13 Nov 2025 08:05:00 -0500
MIME-Version: 1.0
Content-Type: text/html; charset=utf-8
Received-SPF: fail (example)

<html>
  <body>
    <p>Dear customer,</p>
    <p>We noticed suspicious activity on your account. Please <a href="http://secure.example-login.com/verify">verify your account</a> immediately or access will be restricted.</p>
    <p>Regards,<br/>Bank Security Team</p>
  </body>
</html>
'''

bec_email = '''From: ceo@trustedcorp.example.com
To: finance@company.example.com
Subject: Urgent: Wire Transfer Request
Date: Mon, 16 Nov 2025 11:22:00 -0500
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="BOUNDARY123"

--BOUNDARY123
Content-Type: text/plain; charset=utf-8

Hi,
Please arrange an urgent wire transfer of $75,000 to the vendor listed in the attached invoice. Do not discuss this over email.

Regards,
CEO

--BOUNDARY123
Content-Type: application/pdf; name="invoice_457.pdf"
Content-Disposition: attachment; filename="invoice_457.pdf"
Content-Transfer-Encoding: base64

JVBERi0xLjQKJcTl8uXrp/Og0MTGCjEgMCBvYmoK... (truncated sample)
--BOUNDARY123--
'''


def extract_basic_features(raw_email):
    msg = message_from_string(raw_email)
    features = {}
    # Headers
    features['from'] = msg.get('From')
    features['to'] = msg.get('To')
    features['subject'] = msg.get('Subject')
    features['date'] = msg.get('Date')
    features['is_multipart'] = msg.is_multipart()

    # Body and URLs
    body = ''
    urls = []
    num_attachments = 0
    attachment_filenames = []
    for part in msg.walk():
        ctype = part.get_content_type()
        disp = str(part.get('Content-Disposition'))
        if ctype == 'text/plain' and 'attachment' not in disp.lower():
            payload = part.get_payload(decode=True)
            if payload:
                try:
                    body += payload.decode(part.get_content_charset('utf-8'), errors='replace')
                except Exception:
                    body += str(payload)
        elif ctype == 'text/html' and 'attachment' not in disp.lower():
            payload = part.get_payload(decode=True)
            if payload:
                try:
                    body += payload.decode(part.get_content_charset('utf-8'), errors='replace')
                except Exception:
                    body += str(payload)
        elif 'attachment' in disp.lower() or part.get_filename():
            num_attachments += 1
            if part.get_filename():
                attachment_filenames.append(part.get_filename())

    # Extract urls with a simple regex (classroom-safe)
    url_regex = r'https?://[\w\-.\/:]+'
    urls = re.findall(url_regex, body)
    domains = set()
    for u in urls:
        try:
            domains.add(urlparse(u).netloc)
        except Exception:
            continue

    features['num_urls'] = len(urls)
    features['unique_url_domains'] = len(domains)
    features['num_attachments'] = num_attachments
    features['attachment_filenames'] = attachment_filenames
    features['body_snippet'] = (body[:300] + '...') if len(body)>300 else body
    # Heuristic urgency score
    urgency_keywords = ['urgent', 'immediately', 'asap', 'attention']
    features['urgency_score'] = sum(1 for k in urgency_keywords if k in body.lower())

    return features

if __name__ == '__main__':
    for name, raw in [('spam', spam_email), ('phish', phish_email), ('bec', bec_email)]:
        print(f'--- FEATURES for {name} ---')
        f = extract_basic_features(raw)
        for k, v in f.items():
            print(k, ':', v)
        print('\n')
