import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with API key from environment variable
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_overview(input_text):
    prompt = f"""Here are two examples of Overview sections:

Example 1 (VCGamers):
This proposal is for Covena to work with VCGamers to build an AI WhatsApp Shopping Assistant for gaming products. The goal of the AI is to make transactions and shopping within WhatsApp easy and accessible for users.

More about Covena [here](https://drive.google.com/file/d/1SIHZQHPq5nf9a_U0vvdUlhdKRXBlwd4n/view?usp=sharing).

Example 2 (LinkIT360):
This proposal outlines a collaboration between Covena and LinkIT360 to develop an AI-powered customer service solution for the medical healthcare industry. The AI will replace call centers and chat agents, streamlining medical care requests and managing high volumes of inquiries efficiently.

More about Covena [here](https://drive.google.com/file/d/1SIHZQHPq5nf9a_U0vvdUlhdKRXBlwd4n/view?usp=sharing).

Now, generate an Overview section for the following input:

{input_text}

Let's think step by step:
1. Identify the main purpose of the proposal.
2. Determine the companies involved in the collaboration.
3. Summarize the main goal or product to be developed.
4. Include a link to more information about the proposing company.

Now, generate the Overview section:
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates document sections."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

def generate_product(input_text, overview):
    prompt = f"""Here are two examples of Product sections:

Example 1 (VCGamers):
The deliverable will be a conversational AI that assists users in buying and shopping for gaming products via WhatsApp. Users will be able to seamlessly buy products through natural language. It will reference where users can find more details about the products, and provide recommendations based on what the user is looking for.

**Key Features**:
1. **Natural Language Understanding**: The AI comprehends student queries in natural language, allowing for conversational interaction.
2. **Product Catalog Lookup**: The system can access and reference product details, such as gaming gear, accessories, or digital products, and provide users with relevant information.
3. **Seamless Transactions**: Users can complete purchases directly within WhatsApp, without needing to leave the app, through secure and integrated payment options.
4. **Order Tracking & Notifications**: The AI can provide real-time updates on order status, shipping details, and delivery notifications, keeping users informed.
5. **Promotions & Discounts**: The assistant can notify users of special offers, discounts, or exclusive promotions relevant to their gaming needs.
6. **Inventory Check**: The AI can quickly check the availability of products and notify users about in-stock items or upcoming restocks.

*Similar products we've built: [MAP Demo](https://drive.google.com/file/d/1XmKcxvFQP92J_LBPVdQMFnUYDg83ULPk/view?usp=drive_link), [Studilmu WhatsApp Agent](https://drive.google.com/file/d/1Cfo-MYJYlTGErPltz4tCDS_8VvEKWvkJ/view?usp=drive_link), [AYANA Demo](https://drive.google.com/file/d/10qK1HoO_R39EayiKiEoEE41A0-_W9c7U/view?usp=drive_link)*

Example 2 (LinkIT360):
The deliverable is a conversational AI system that handles medical home care inquiries. It will assist patients by booking home doctor visits and addressing common medical home care questions. The system will provide prompt responses in natural language, ensuring seamless patient communication and reducing human agents' workload.

**Key Features**:
1. **Natural Language Understanding**: The AI will comprehend and respond to patient queries in natural language, allowing for conversational and efficient communication.
2. **Home Care Booking**: Patients can request a doctor to visit their home, and the AI will manage appointment bookings, confirming availability and scheduling.
3. **Medical Queries Management**: The AI will handle queries related to home care services, such as doctor availability, service coverage, and medical support details.
4. **Multilingual Support**: The AI can support English and Indonesian.
5. **Seamless Human Handover**: For complex cases, the AI can transfer conversations to human agents, ensuring smooth transitions when needed.

*Similar products we've built: [MAP Demo](https://drive.google.com/file/d/1XmKcxvFQP92J_LBPVdQMFnUYDg83ULPk/view?usp=drive_link), [Studilmu WhatsApp Agent](https://drive.google.com/file/d/1Cfo-MYJYlTGErPltz4tCDS_8VvEKWvkJ/view?usp=drive_link), [AYANA Demo](https://drive.google.com/file/d/10qK1HoO_R39EayiKiEoEE41A0-_W9c7U/view?usp=drive_link)*

Now, generate a Product section based on the following Overview and input:

Overview:
{overview}

Input:
{input_text}

Let's think step by step:
1. Describe the main deliverable or product based on the overview and input.
2. List 4-6 key features of the product, ensuring they align with the main goal.
3. Mention the similar products built by the company. 

Now, generate the Product section:
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates document sections."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

def generate_examples(input_text, overview, product):
    prompt = f"""Here are example interactions from two different proposals:

VCGamers Example:
**Example 1 (user buys in game items)**
**User Query**: "Aku mau beli 300 gems Clash of Clans sekarang."
**AI Response**: "Baik! 300 gems harganya Rp50.000. Kamu bisa langsung melakukan pembayaran melalui link ini: [link pembayaran]. Setelah selesai, konfirmasinya akan langsung dikirim ke WhatsApp dan gems akan masuk ke akun kamu."
**AI Response**: "Pembayaran berhasil! Gems akan segera masuk ke akunmu. Terima kasih sudah berbelanja, selamat bermain!"

LinkIT360 Example:
**Example 1 (user books a home doctor visit)**
**User Query**: "I need a doctor to visit my home, can I book one now?"
**AI Response**: "Sure! Could you please provide your address and preferred time? I will check for the nearest available doctor for you."
**User Follow-Up**: "My address is Jalan Kelapa Nias XII, and I need a doctor by 4 PM."
**AI Response**: "Great, I'm checking availability.... The doctor is available, you can finalize your booking through this link: [booking link]."

Now, generate an Examples section with Sample Case Study Interactions based on the following Overview and Product sections:

Overview:
{overview}

Product:
{product}

Input:
{input_text}

Let's think step by step:
1. Identify the key features and use cases mentioned in the Product section.
2. Create 5-7 example interactions that demonstrate these features.
3. Ensure the interactions show realistic conversations between users and the AI.
4. Include follow-up questions and AI responses to show the depth of the AI's capabilities.
5. Demonstrate how the AI handles bookings, payments, or other relevant actions.
6. Make sure the examples cover a variety of scenarios relevant to the product.
7. Follow through the conversation naturally and to the end of the flow.

Now, generate the Examples section:
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates document sections."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

def edit_section(current_content, edit_suggestion):
    prompt = f"""You are an AI assistant tasked with editing a section of a proposal document.
    Here's the current content of the section:

    {current_content}

    The user has suggested the following edit:

    {edit_suggestion}

    Please update the section based on this suggestion. Maintain the overall structure and style of the original content,
    but incorporate the user's suggestions as appropriate. If the suggestion is unclear or doesn't fit well with the 
    existing content, use your best judgment to make improvements while keeping the original intent.

    Provide the updated section:
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that edits document sections."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()