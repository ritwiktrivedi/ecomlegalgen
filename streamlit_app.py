import streamlit as st
import os
import base64
from datetime import datetime


def main():
    last_updated = datetime.now().strftime("%B %d, %Y")
    st.set_page_config(page_title="Store Terms Generator", layout="wide")

    st.title("Store Terms Generator")
    st.markdown(
        "Fill in the form below to generate customized store terms documents.")

    st.markdown(
        "These terms are templates and should be reviewed by a legal professional before use.")

    st.markdown("These terms have been made around Razorpay and Shopify, if you are using any other payment gateway or ecommerce service, please change the terms accordingly.")

    # Form for collecting company information
    with st.form("company_info_form"):
        st.subheader("Company Information")
        col1, col2 = st.columns(2)

        with col1:
            company_name = st.text_input("Company Name")
            website_url = st.text_input("Website URL like example.com")
            jurisdiction = st.text_input(
                "Jurisdiction (e.g., Dehradun, Uttarakhand)")

        with col2:
            company_contact_email = st.text_input("Company Contact Email")
            privacy_compliance_email = st.text_input(
                "Privacy Compliance Email")
            refund_timeframe = st.slider(
                "Refund Timeframe (in days)", min_value=1, value=10, max_value=30)
            refund_timeframe = int(refund_timeframe)

        # Additional options
        st.subheader("Select Documents to Generate")
        generate_refund = st.checkbox("Shipping and Return Policy", value=True)
        generate_privacy = st.checkbox("Privacy Policy", value=True)
        generate_terms = st.checkbox("Terms and Conditions", value=True)

        submit_button = st.form_submit_button("Generate Documents")

    if submit_button:
        if not company_name or not company_contact_email or not website_url or not privacy_compliance_email or not jurisdiction:
            st.error("Please fill in all required fields.")
        else:
            # Generate the selected documents
            if generate_refund:
                refund_policy = generate_refund_policy(
                    company_name, company_contact_email, refund_timeframe, last_updated)
                display_document_with_download(
                    "Shipping and Return Policy", refund_policy)

            if generate_privacy:
                privacy_policy = generate_privacy_policy(
                    company_name, company_contact_email, last_updated, website_url, privacy_compliance_email)
                display_document_with_download(
                    "Privacy Policy", privacy_policy)

            if generate_terms:
                terms_conditions = generate_terms_conditions(
                    company_name, company_contact_email, last_updated, website_url, jurisdiction)
                display_document_with_download(
                    "Terms and Conditions", terms_conditions)


def generate_refund_policy(company_name, company_contact_email, refund_timeframe, last_updated):
    refund_template = """**Shipping and Return Policy**

**Last Updated:** {last_updated}

# For Domestic B2C Orders (Within India)

**Shipping Policy**

We offer two types of orders:

1. Made-on-Order: 
Ships within 15-28 days from payment.

2. Ready-to-Ship: 
The orders are processed manually for shipping and may take upto 48 hrs in case of high volumes. 
The estimated delivery time is 5-7 business days from the moment the order is processed. 
The exact delivery time will depend on courier partners and information regarding the same shall be mailed as 
soon as the order is processed.
Delivery time depends on the courier, and tracking details are provided once the order is shipped.


**Returns**

Our returns and refunds policy lasts {refund_timeframe} days. If your product was damaged in transit,
 send a photo on the delivery day to {company_contact_email} for a refund or replacement.
 (An extension of 1 day may be given on a case by case basis but this is a must for processing the refund or replacement request).

For ready to ship orders, if {refund_timeframe} days have gone by since your 
purchase or when the item(s) was(were) delivered (whichever is later),
unfortunately we can't offer you a refund or exchange.

Custom/On-Order items (B2C non bulk or less than 50 pcs) are returnable only for damage or quality issues.
We offer a partial refund or replacement (which may take 15-28 days).
Exchanges are only for the original product(s) in the order.

If an item appears to be intentionally damaged, only a partial refund will be issued, with no exchange as decided at our sole discretion.

To be eligible for a return, your item must be unused and in the same
condition that you received it. It must also be in the original
packaging.

Several types of goods are exempt from being returned. Perishable goods
such as food, flowers, newspapers or magazines cannot be returned. We
also do not accept products that are intimate or sanitary goods,
hazardous materials, or flammable liquids or gases.

Additional non-returnable items:

-   Gift cards (refer section 6A of Terms and Conditions)

-   Downloadable software products

-   Some health and personal care items

To complete your return, we require a receipt or proof of purchase.

Please do not send your purchase back to the manufacturer.

There are certain situations where only partial refunds are granted: (if
applicable)

Book with obvious signs of use

CD, DVD, VHS tape, software, video game, cassette tape, or vinyl record
that has been opened.

Any item not in its original condition, is damaged or missing parts for
reasons not due to our error.

Any item that is returned more than {refund_timeframe} days after delivery

**Refunds (if applicable)**

Once your return is received and inspected, we will send you an email to
notify you that we have received your returned item. We will also notify
you of the approval or rejection of your refund.

If you are approved, then your refund will be processed, and a credit
will automatically be applied to your credit card or original method of
payment, within a certain amount of days.

**Late or missing refunds (if applicable)**

If you haven't received a refund yet, first check your bank account
again.

Then contact your credit card company, it may take some time before your
refund is officially posted.

Next contact your bank. There is often some processing time before a
refund is posted.

If you've done all of this and you still have not received your refund
yet, please contact us at {company_contact_email}.

**Sale items (if applicable)**

Only regular priced items may be refunded, unfortunately sale items
cannot be refunded.

**Exchanges (if applicable)**

We only replace items if they are defective or damaged. If you need to
exchange it for the same item, send us an email at {company_contact_email} and send your item to the address provided in the email by the support team.

**Gifts**

If the item was marked as a gift when purchased and shipped directly to
you, you'll receive a gift credit for the value of your return. Once the
returned item is received, a gift certificate will be mailed to you.

If the item wasn't marked as a gift when purchased, or the gift giver
had the order shipped to themselves to give to you later, we will send a
refund to the gift giver and he will find out about your return.

**Shipping**

To return your product, you should contact us at {company_contact_email} and then mail the items to the address provided in the email
by the support team.

You will be responsible for paying for your own shipping costs for
returning your item. Shipping costs are non-refundable. If you receive a
refund, the cost of return shipping will be deducted from your refund.

Depending on where you live, the time it may take for your exchanged
product to reach you, may vary.

If you are shipping an item over INR 5000, you should consider using a
trackable shipping service or purchasing shipping insurance. We don't
guarantee that we will receive your returned item.

# For B2B, International B2B and B2C Bulk orders

We currently ship only within India for standard B2C orders but are shipping internationally on case by case basis for bulk orders placed via email upon mutual acceptance of the terms of the B2B or a bulk B2C sale transaction.
The shipping terms will be negotiated on a per transaction/order basis as may be agreed upon mutually."""

    return refund_template.format(
        company_contact_email=company_contact_email,
        refund_timeframe=refund_timeframe,
        last_updated=last_updated
    )


def generate_privacy_policy(company_name, company_contact_email, last_updated, website_url, privacy_compliance_email):
    privacy_template = """PRIVACY POLICY

**Last Updated:** {last_updated}

This Privacy Policy describes how **{company_name}** (the "Site", "we", "us", or "our") collects, uses, and discloses your personal information when you visit, use our services, or make a purchase from {website_url} (the "Site") or otherwise communicate with us regarding the Site (collectively, the "Services"). For purposes of this Privacy Policy, "you" and "your" means you as the user of the Services, whether you are a customer, website visitor, or another individual whose information we have collected pursuant to this Privacy Policy.

Please read this Privacy Policy carefully. By using and accessing any of the Services, you agree to the collection, use, and disclosure of your information as described in this Privacy Policy. If you do not agree to this Privacy Policy, please do not use or access any of the Services.

**SECTION 1 - WHAT DO WE DO WITH YOUR INFORMATION?**

When you purchase something from our store, as part of the buying and
selling process, we collect the personal information you give us such as
your name, address and email address.

When you browse our store, we also automatically receive your computer's
internet protocol (IP) address in order to provide us with information
that helps us learn about your browser and operating system.

Email marketing: With your permission, we may send you
emails about our store, new products and other updates.

**SECTION 2 - CONSENT**

How do you get my consent?

When you provide us with personal information to complete a transaction,
verify your credit card, place an order, arrange for a delivery or
return a purchase, we imply that you consent to our collecting it and
using it for that specific reason only.

If we ask for your personal information for a secondary reason, like
marketing, we will either ask you directly for your expressed consent,
or provide you with an opportunity to say no.

How do I withdraw my consent?

If after you opt-in, you change your mind, you may withdraw your consent
for us to contact you, for the continued collection, use or disclosure
of your information, at anytime, by contacting us at {privacy_compliance_email}.

**SECTION 3 - DISCLOSURE**

In certain circumstances, we may disclose your personal information to third parties for contract fulfillment purposes, legitimate purposes and other reasons subject to this Privacy Policy. Such circumstances may include:

- With vendors or other third parties who perform services on our behalf (e.g., IT management, payment processing, data analytics, customer support, cloud storage, fulfillment and shipping).
- With business and marketing partners to provide services and advertise to you. Our business and marketing partners will use your information in accordance with their own privacy notices.
- When you direct, request us or otherwise consent to our disclosure of certain information to third parties, such as to ship you products or through your use of social media widgets or login integrations, with your consent.
- With our affiliates or otherwise within our corporate group, in our legitimate interests to run a successful business.
- In connection with a business transaction such as a merger or bankruptcy, to comply with any applicable legal obligations (including to respond to subpoenas, search warrants and similar requests), to enforce any applicable terms of service, and to protect or defend the Services, our rights, and the rights of our users or others.

We disclose the following categories of personal information and sensitive personal information about users for the purposes set out above in *"How we Collect and Use your Personal Information"* and *"How we Disclose Personal Information"*:

| Category | Categories of Recipients |
|----------|--------------------------|
| - Identifiers such as basic contact details and certain order and account information<br>- Commercial information such as order information, shopping information and customer support information<br>- Internet or other similar network activity, such as Usage Data<br>- Geolocation data such as locations determined by an IP address or other technical measures | - Vendors and third parties who perform services on our behalf (such as Internet service providers, payment processors, fulfillment partners, customer support partners and data analytics providers)<br>- Business and marketing partners<br>- Affiliates |

We do not use or disclose sensitive personal information without your consent or for the purposes of inferring characteristics about you.

**SECTION 4 - PAYMENT**

We use Razorpay for processing payments. We/Razorpay do not store your
card data on their servers. The data is encrypted through the Payment
Card Industry Data Security Standard (PCI-DSS) when processing payment.
Your purchase transaction data is only used as long as is necessary to
complete your purchase transaction. After that is complete, your
purchase transaction information is not saved.

Our payment gateway adheres to the standards set by PCI-DSS as managed
by the PCI Security Standards Council, which is a joint effort of brands
like Visa, MasterCard, American Express and Discover.

PCI-DSS requirements help ensure the secure handling of credit card
information by our store and its service providers.

For more insight, you may also want to read terms and conditions of
razorpay on https://razorpay.com

**SECTION 5 - THIRD-PARTY SERVICES**

In general, the third-party providers used by us will only collect, use
and disclose your information to the extent necessary to allow them to
perform the services they provide to us.

However, certain third-party service providers, such as payment gateways
and other payment transaction processors, have their own privacy
policies in respect to the information we are required to provide to
them for your purchase-related transactions.

For these providers, we recommend that you read their privacy policies
so you can understand the manner in which your personal information will
be handled by these providers.

In particular, remember that certain providers may be located in or have
facilities that are located a different jurisdiction than either you or
us. So if you elect to proceed with a transaction that involves the
services of a third-party service provider, then your information may
become subject to the laws of the jurisdiction(s) in which that service
provider or its facilities are located.

Once you leave our store's website or are redirected to a third-party
website or application, you are no longer governed by this Privacy
Policy or our website's Terms of Service.

Links:

When you click on links on our store, they may direct you away from our
site. We are not responsible for the privacy practices of other sites
and encourage you to read their privacy statements.

**SECTION 6 - SECURITY**

To protect your personal information, we take reasonable precautions and
follow industry best practices to make sure it is not inappropriately
lost, misused, accessed, disclosed, altered or destroyed.

**SECTION 7 - COOKIES**

We use cookies to maintain session of your user account. It is not used to personally identify you on other websites. For specific information about the Cookies that we use related to powering our store with Shopify, see [https://www.shopify.com/legal/cookies](https://www.shopify.com/legal/cookies). We use Cookies to power and improve our Site and our Services (including to remember your actions and preferences), to run analytics and better understand user interaction with the Services (in our legitimate interests to administer, improve and optimize the Services). We may also permit third parties and services providers to use Cookies on our Site to better tailor the services, products and advertising on our Site and other websites.

Most browsers automatically accept Cookies by default, but you can choose to set your browser to remove or reject Cookies through your browser controls. Please keep in mind that removing or blocking Cookies can negatively impact your user experience and may cause some of the Services, including certain features and general functionality, to work incorrectly or no longer be available. Additionally, blocking Cookies may not completely prevent how we share information with third parties such as our advertising partners.

**SECTION 8 - AGE OF CONSENT**

By using this site, you represent that you are at least the age of
majority in your state or province of residence, or that you are the age
of majority in your state or province of residence and you have given us
your consent to allow any of your minor dependents to use this site.

**SECTION 9 - CHANGES TO THIS PRIVACY POLICY**

We reserve the right to modify this privacy policy at any time, so
please review it frequently. Changes and clarifications will take effect
immediately upon their posting on the website. If we make material
changes to this policy, we will notify you here that it has been
updated, so that you are aware of what information we collect, how we
use it, and under what circumstances, if any, we use and/or disclose it.

If our store is acquired or merged with another company, your
information may be transferred to the new owners so that we may continue
to sell products to you.

**QUESTIONS AND CONTACT INFORMATION**

If you would like to: access, correct, amend or delete any personal
information we have about you, register a complaint, or simply want more
information contact our Privacy Compliance Team at {privacy_compliance_email}.

----"""

    return privacy_template.format(
        company_name=company_name,
        company_contact_email=company_contact_email,
        last_updated=last_updated,
        website_url=website_url,
        privacy_compliance_email=privacy_compliance_email,
    )


def generate_terms_conditions(company_name, company_contact_email, last_updated, website_url, jurisdiction):
    terms_template = """TERMS OF SERVICE

**Last Updated:** {last_updated}

**OVERVIEW**

This website is operated by **{company_name}**. Throughout
the site, the terms "we", "us" and "our" refer to **{company_name}**. **{company_name}** offers this website,
including all information, tools and services available from this site
to you, the user, conditioned upon your acceptance of all terms,
conditions, policies and notices stated here.

By visiting our site and/ or purchasing something from us, you engage in
our "Service" and agree to be bound by the following terms and
conditions ("Terms of Service", "Terms"), including those additional
terms and conditions and policies referenced herein and/or available by
hyperlink. These Terms of Service apply to all users of the site,
including without limitation users who are browsers, vendors, customers,
merchants, and/ or contributors of content.

Please read these Terms of Service carefully before accessing or using
our website. By accessing or using any part of the site, you agree to be
bound by these Terms of Service. If you do not agree to all the terms
and conditions of this agreement, then you may not access the website or
use any services. If these Terms of Service are considered an offer,
acceptance is expressly limited to these Terms of Service.

Any new features or tools which are added to the current store shall
also be subject to the Terms of Service. You can review the most current
version of the Terms of Service at any time on this page. We reserve the
right to update, change or replace any part of these Terms of Service by
posting updates and/or changes to our website. It is your responsibility
to check this page periodically for changes. Your continued use of or
access to the website following the posting of any changes constitutes
acceptance of those changes.

**SECTION 1 - ONLINE STORE TERMS**

By agreeing to these Terms of Service, you represent that you are at
least the age of majority in your state or province of residence, or
that you are the age of majority in your state or province of residence
and you have given us your consent to allow any of your minor dependents
to use this site.

You may not use our products for any illegal or unauthorized purpose nor
may you, in the use of the Service, violate any laws in your
jurisdiction (including but not limited to copyright laws).

You must not transmit any worms or viruses or any code of a destructive
nature.

A breach or violation of any of the Terms will result in an immediate
termination of your Services.

**SECTION 2 - GENERAL CONDITIONS**

We reserve the right to refuse service to anyone for any reason at any
time.

You understand that your content (not including credit card
information), may be transferred unencrypted and involve (a)
transmissions over various networks; and (b) changes to conform and
adapt to technical requirements of connecting networks or devices.
Credit card information is always encrypted during transfer over
networks.

You agree not to reproduce, duplicate, copy, sell, resell or exploit any
portion of the Service, use of the Service, or access to the Service or
any contact on the website through which the service is provided,
without express written permission by us.

The headings used in this agreement are included for convenience only
and will not limit or otherwise affect these Terms.

**SECTION 3 - ACCURACY, COMPLETENESS AND TIMELINESS OF INFORMATION**

We are not responsible if information made available on this site is not
accurate, complete or current. The material on this site is provided for
general information only and should not be relied upon or used as the
sole basis for making decisions without consulting primary, more
accurate, more complete or more timely sources of information. Any
reliance on the material on this site is at your own risk.

This site may contain certain historical information. Historical
information, necessarily, is not current and is provided for your
reference only. We reserve the right to modify the contents of this site
at any time, but we have no obligation to update any information on our
site. You agree that it is your responsibility to monitor changes to our
site.

**SECTION 4 - MODIFICATIONS TO THE SERVICE AND PRICES**

Prices for our products are subject to change without notice.

We reserve the right at any time to modify or discontinue the Service
(or any part or content thereof) without notice at any time.

We shall not be liable to you or to any third-party for any
modification, price change, suspension or discontinuance of the Service.

**SECTION 5 - PRODUCTS OR SERVICES**

Certain products or services may be available exclusively online through
the website. These products or services may have limited quantities and
are subject to return or exchange only according to our Return Policy.

We have made every effort to display as accurately as possible the
colors and images of our products that appear at the store. We cannot
guarantee that your computer monitor's display of any color will be
accurate.

We reserve the right, but are not obligated, to limit the sales of our
products or Services to any person, geographic region or jurisdiction.
We may exercise this right on a case-by-case basis. We reserve the right
to limit the quantities of any products or services that we offer. All
descriptions of products or product pricing are subject to change at
anytime without notice, at the sole discretion of us. We reserve the
right to discontinue any product at any time. Any offer for any product
or service made on this site is void where prohibited.

We do not warrant that the quality of any products, services,
information, or other material purchased or obtained by you will meet
your expectations, or that any errors in the Service will be corrected.

**SECTION 6 - ACCURACY OF BILLING AND ACCOUNT INFORMATION**

We reserve the right to refuse any order you place with us. We may, in
our sole discretion, limit or cancel quantities purchased per person,
per household or per order. These restrictions may include orders placed
by or under the same customer account, the same credit card, and/or
orders that use the same billing and/or shipping address. In the event
that we make a change to or cancel an order, we may attempt to notify
you by contacting the e-mail and/or billing address/phone number
provided at the time the order was made. We reserve the right to limit
or prohibit orders that, in our sole judgment, appear to be placed by
dealers, resellers or distributors.

You agree to provide current, complete and accurate purchase and account
information for all purchases made at our store. You agree to promptly
update your account and other information, including your email address
and credit card numbers and expiration dates, so that we can complete
your transactions and contact you as needed.

For more detail, please review our Returns Policy.

**SECTION 6A - GIFT CARDS**

Gift Cards issued by {company_name} are redeemable solely on our website {website_url}. Gift Cards cannot be redeemed for cash, reloaded, resold, transferred for value, or used to purchase other gift cards, unless required by law.
Gift Cards must be used within their validity period as defined at the time of purchase. In India, unless otherwise stated, the default validity is 3 years from the date of issue in compliance with applicable Reserve Bank of India (RBI) guidelines on prepaid payment instruments.
Lost, stolen, or unauthorized use of gift cards is the sole responsibility of the purchaser or holder. We are not responsible for lost or stolen gift cards or their unauthorized use.
Any unused balance on a Gift Card after expiry shall be forfeited and will not be refunded.
By purchasing, redeeming, or using a Gift Card, you agree to be bound by these terms and any other terms provided with the Gift Card. {company_name} reserves the right to modify the terms and conditions of Gift Card usage at its discretion, in compliance with Indian law.

**SECTION 7 - OPTIONAL TOOLS**

We may provide you with access to third-party tools over which we
neither monitor nor have any control nor input.

You acknowledge and agree that we provide access to such tools "as is"
and "as available" without any warranties, representations or conditions
of any kind and without any endorsement. We shall have no liability
whatsoever arising from or relating to your use of optional third-party
tools.

Any use by you of optional tools offered through the site is entirely at
your own risk and discretion and you should ensure that you are familiar
with and approve of the terms on which tools are provided by the
relevant third-party provider(s).

We may also, in the future, offer new services and/or features through
the website (including, the release of new tools and resources). Such
new features and/or services shall also be subject to these Terms of
Service.

**SECTION 8 - THIRD-PARTY LINKS**

Certain content, products and services available via our Service may
include materials from third-parties.

Third-party links on this site may direct you to third-party websites
that are not affiliated with us. We are not responsible for examining or
evaluating the content or accuracy and we do not warrant and will not
have any liability or responsibility for any third-party materials or
websites, or for any other materials, products, or services of
third-parties.

We are not liable for any harm or damages related to the purchase or use
of goods, services, resources, content, or any other transactions made
in connection with any third-party websites. Please review carefully the
third-party's policies and practices and make sure you understand them
before you engage in any transaction. Complaints, claims, concerns, or
questions regarding third-party products should be directed to the
third-party.

**SECTION 9 - USER COMMENTS, FEEDBACK AND OTHER SUBMISSIONS**

If, at our request, you send certain specific submissions (for example
contest entries) or without a request from us you send creative ideas,
suggestions, proposals, plans, or other materials, whether online, by
email, by postal mail, or otherwise (collectively, 'comments'), you
agree that we may, at any time, without restriction, edit, copy,
publish, distribute, translate and otherwise use in any medium any
comments that you forward to us. We are and shall be under no obligation
(1) to maintain any comments in confidence; (2) to pay compensation for
any comments; or (3) to respond to any comments.

We may, but have no obligation to, monitor, edit or remove content that
we determine in our sole discretion are unlawful, offensive,
threatening, libelous, defamatory, pornographic, obscene or otherwise
objectionable or violates any party's intellectual property or these
Terms of Service.

You agree that your comments will not violate any right of any
third-party, including copyright, trademark, privacy, personality or
other personal or proprietary right. You further agree that your
comments will not contain libelous or otherwise unlawful, abusive or
obscene material, or contain any computer virus or other malware that
could in any way affect the operation of the Service or any related
website. You may not use a false e-mail address, pretend to be someone
other than yourself, or otherwise mislead us or third-parties as to the
origin of any comments. You are solely responsible for any comments you
make and their accuracy. We take no responsibility and assume no
liability for any comments posted by you or any third-party.

**SECTION 10 - PERSONAL INFORMATION**

Your submission of personal information through the store is governed by
our Privacy Policy.

**SECTION 11 - ERRORS, INACCURACIES AND OMISSIONS**

Occasionally there may be information on our site or in the Service that
contains typographical errors, inaccuracies or omissions that may relate
to product descriptions, pricing, promotions, offers, product shipping
charges, transit times and availability. We reserve the right to correct
any errors, inaccuracies or omissions, and to change or update
information or cancel orders if any information in the Service or on any
related website is inaccurate at any time without prior notice
(including after you have submitted your order).

We undertake no obligation to update, amend or clarify information in
the Service or on any related website, including without limitation,
pricing information, except as required by law. No specified update or
refresh date applied in the Service or on any related website, should be
taken to indicate that all information in the Service or on any related
website has been modified or updated.

**SECTION 12 - PROHIBITED USES**

In addition to other prohibitions as set forth in the Terms of Service,
you are prohibited from using the site or its content: (a) for any
unlawful purpose; (b) to solicit others to perform or participate in any
unlawful acts; (c) to violate any international, federal, provincial or
state regulations, rules, laws, or local ordinances; (d) to infringe
upon or violate our intellectual property rights or the intellectual
property rights of others; (e) to harass, abuse, insult, harm, defame,
slander, disparage, intimidate, or discriminate based on gender, sexual
orientation, religion, ethnicity, race, age, national origin, or
disability; (f) to submit false or misleading information; (g) to upload
or transmit viruses or any other type of malicious code that will or may
be used in any way that will affect the functionality or operation of
the Service or of any related website, other websites, or the Internet;
(h) to collect or track the personal information of others; (i) to spam,
phish, pharm, pretext, spider, crawl, or scrape; (j) for any obscene or
immoral purpose; or (k) to interfere with or circumvent the security
features of the Service or any related website, other websites, or the
Internet. We reserve the right to terminate your use of the Service or
any related website for violating any of the prohibited uses.

**SECTION 13 - DISCLAIMER OF WARRANTIES; LIMITATION OF LIABILITY**

We do not guarantee, represent or warrant that your use of our service
will be uninterrupted, timely, secure or error-free.

We do not warrant that the results that may be obtained from the use of
the service will be accurate or reliable.

You agree that from time to time we may remove the service for
indefinite periods of time or cancel the service at any time, without
notice to you.

You expressly agree that your use of, or inability to use, the service
is at your sole risk. The service and all products and services
delivered to you through the service are (except as expressly stated by
us) provided 'as is' and 'as available' for your use, without any
representation, warranties or conditions of any kind, either express or
implied, including all implied warranties or conditions of
merchantability, merchantable quality, fitness for a particular purpose,
durability, title, and non-infringement.

In no case shall **{company_name}**, our directors,
officers, employees, affiliates, agents, contractors, interns,
suppliers, service providers or licensors be liable for any injury,
loss, claim, or any direct, indirect, incidental, punitive, special, or
consequential damages of any kind, including, without limitation lost
profits, lost revenue, lost savings, loss of data, replacement costs, or
any similar damages, whether based in contract, tort (including
negligence), strict liability or otherwise, arising from your use of any
of the service or any products procured using the service, or for any
other claim related in any way to your use of the service or any
product, including, but not limited to, any errors or omissions in any
content, or any loss or damage of any kind incurred as a result of the
use of the service or any content (or product) posted, transmitted, or
otherwise made available via the service, even if advised of their
possibility. Because some states or jurisdictions do not allow the
exclusion or the limitation of liability for consequential or incidental
damages, in such states or jurisdictions, our liability shall be limited
to the maximum extent permitted by law.

**SECTION 14 - INDEMNIFICATION**

You agree to indemnify, defend and hold harmless **{company_name}** and our parent, subsidiaries, affiliates, partners,
officers, directors, agents, contractors, licensors, service providers,
subcontractors, suppliers, interns and employees, harmless from any
claim or demand, including reasonable attorneys' fees, made by any
third-party due to or arising out of your breach of these Terms of
Service or the documents they incorporate by reference, or your
violation of any law or the rights of a third-party.

**SECTION 15 - SEVERABILITY**

In the event that any provision of these Terms of Service is determined
to be unlawful, void or unenforceable, such provision shall nonetheless
be enforceable to the fullest extent permitted by applicable law, and
the unenforceable portion shall be deemed to be severed from these Terms
of Service, such determination shall not affect the validity and
enforceability of any other remaining provisions.

**SECTION 16 - TERMINATION**

The obligations and liabilities of the parties incurred prior to the
termination date shall survive the termination of this agreement for all
purposes.

These Terms of Service are effective unless and until terminated by
either you or us. You may terminate these Terms of Service at any time
by notifying us that you no longer wish to use our Services, or when you
cease using our site.

If in our sole judgment you fail, or we suspect that you have failed, to
comply with any term or provision of these Terms of Service, we also may
terminate this agreement at any time without notice and you will remain
liable for all amounts due up to and including the date of termination;
and/or accordingly may deny you access to our Services (or any part
thereof).

**SECTION 17 - ENTIRE AGREEMENT**

The failure of us to exercise or enforce any right or provision of these
Terms of Service shall not constitute a waiver of such right or
provision.

These Terms of Service and any policies or operating rules posted by us
on this site or in respect to The Service constitutes the entire
agreement and understanding between you and us and govern your use of
the Service, superseding any prior or contemporaneous agreements,
communications and proposals, whether oral or written, between you and
us (including, but not limited to, any prior versions of the Terms of
Service).

Any ambiguities in the interpretation of these Terms of Service shall
not be construed against the drafting party.

**SECTION 18 - GOVERNING LAW**

These Terms of Service and any separate agreements whereby we provide
you Services shall be governed by and construed in accordance with the
laws of India and jurisdiction of **{jurisdiction}**.

**SECTION 19 - CHANGES TO TERMS OF SERVICE**

You can review the most current version of the Terms of Service at any
time at this page.

We reserve the right, at our sole discretion, to update, change or
replace any part of these Terms of Service by posting updates and
changes to our website. It is your responsibility to check our website
periodically for changes. Your continued use of or access to our website
or the Service following the posting of any changes to these Terms of
Service constitutes acceptance of those changes.

**SECTION 20 - CONTACT INFORMATION**

Questions about the Terms of Service should be sent to us at
{company_contact_email}.

---------------------------------"""

    return terms_template.format(
        company_name=company_name,
        company_contact_email=company_contact_email,
        last_updated=last_updated,
        website_url=website_url,
        jurisdiction=jurisdiction
    )


def display_document_with_download(title, content):
    st.markdown(f"## {title}")

    # Creating an expander to show/hide the document content
    with st.expander("View Document", expanded=False):
        st.markdown(content, unsafe_allow_html=True)

    # Offering a download button
    b64_content = base64.b64encode(content.encode()).decode()
    file_name = f"{title.lower().replace(' ', '_')}.md"

    href = f'<a href="data:file/markdown;base64,{b64_content}" download="{file_name}" class="download-button">Download {title}</a>'
    st.markdown(href, unsafe_allow_html=True)

    # Add a horizontal line for visual separation
    st.markdown("---")


if __name__ == "__main__":
    main()
