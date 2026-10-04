import warnings

from nicegui import ui

from scam_data import scam_alerts

from translations import translations
# --------------------------------------------------
# Page settings
# --------------------------------------------------

ui.page_title('ScamShield')

ui.colors(
    primary='#1f4e79',
    secondary='#5c677d',
    accent='#d9534f'
)


# --------------------------------------------------
# Navigation bar
# --------------------------------------------------

with ui.row().classes(
    'w-full items-center justify-between px-10 py-5 bg-white shadow-sm'
):

    ui.label('ScamShield').classes(
        'text-2xl font-bold text-primary'
    )

    with ui.row().classes('gap-8 items-center'):

        home_link = ui.link(
    'Home',
    '#top'
).classes(
    'text-gray-700'
)
        
        scam_alerts_link = ui.link(
    'Scam Alerts',
    '#scam-alerts'
).classes(
    'text-gray-700'
)

        learn_link = ui.link(
    'Learn',    
    '#learn'
).classes(
    'text-gray-700'
)

        check_message_link = ui.link(
    'Check a Message',
    '#message-checker'
).classes(
    'text-gray-700'
)

        report_scam_link = ui.link(
    'Report a Scam',
    '#report-scam'
).classes(
    'text-gray-700'
)

        language_selector = ui.select(
            list(translations.keys()),
            value='English',
            label='Language'
        ).classes('w-40')

def change_language():

    language = language_selector.value
    selected = translations[language]

    home_link.set_text(selected['home'])
    scam_alerts_link.set_text(selected['scam_alerts'])
    learn_link.set_text(selected['learn'])
    check_message_link.set_text(selected['check_message'])
    report_scam_link.set_text(selected['report_scam'])

    hero_title.set_text(selected['hero_title'])
    hero_description.set_text(selected['hero_description'])

    know_scams_title.set_text(
    selected['know_scams_title']
)

    know_scams_description.set_text(
        selected['know_scams_description']
    )

    banking_card['title'].set_text(
        selected['banking_scams']
    )

    phishing_card['title'].set_text(
        selected['phishing']
    )

    delivery_card['title'].set_text(
        selected['delivery_scams']
    )

    investment_card['title'].set_text(
        selected['investment_scams']
    )

    banking_card['description'].set_text(
        selected['banking_description']
    )

    phishing_card['description'].set_text(
        selected['phishing_description']
    )

    delivery_card['description'].set_text(
        selected['delivery_description']
    )

    investment_card['description'].set_text(
        selected['investment_description']
    )

    banking_card['warning_signs'].set_text(
        selected['banking_warning']
    )

    phishing_card['warning_signs'].set_text(
        selected['phishing_warning']
    )

    delivery_card['warning_signs'].set_text(
        selected['delivery_warning']
    )

    investment_card['warning_signs'].set_text(
        selected['investment_warning']
    )

    explore_alerts_button.set_text(
        selected['explore_alerts']
    )

    check_message_button.set_text(
        selected['check_message_button']
    )

    checker_title.set_text(
        selected['checker_title']
    )

    checker_description.set_text(
        selected['checker_description']
    )

    checker_button.set_text(
        selected['checker_button']
    )

    message_input.props(
    f'placeholder="{selected["checker_placeholder"]}"'
)

language_selector.on_value_change(
    lambda: change_language()
)

# --------------------------------------------------
# Hero section
# --------------------------------------------------

with ui.column().props(
    'id=top'
).classes(
    'w-full items-center text-center py-24 px-6 bg-gray-50'
):

    hero_title = ui.label(
        'Protect yourself from scams'
    ).classes(
        'text-5xl font-bold text-gray-900 max-w-3xl'
    )

    hero_description = ui.label(
        'Understand the latest scams, recognize warning signs, '
        'and make safer decisions online.'
    ).classes(
        'text-xl text-gray-600 max-w-2xl mt-5 leading-relaxed'
    )

    with ui.row().classes(
        'gap-4 mt-10 justify-center flex-nowrap'
    ):

        explore_alerts_button = ui.button(
            'Explore Scam Alerts'
        ).props(
            'unelevated'
        ).classes(
            'whitespace-nowrap'
        )

        check_message_button = ui.button(
            'Check a Message'
        ).props(
            'outline'
        ).classes(
            'whitespace-nowrap'
        )

        explore_alerts_button.on_click(
    lambda: ui.navigate.to('#scam-alerts')
)

check_message_button.on_click(
    lambda: ui.navigate.to('#message-checker')
)


# --------------------------------------------------
# Scam categories
# --------------------------------------------------

with ui.column().classes(
    'w-full items-center py-20 px-6'
):

    know_scams_title = ui.label(
    'Know the scams'
).classes(
    'text-3xl font-bold text-gray-900'
)

know_scams_description = ui.label(
    'Learn how common scams work and what warning signs to look for.'
).classes(
    'text-lg text-gray-600 text-center mt-3 max-w-2xl'
)


def create_scam_card(title, description, warning_signs, details):

    with ui.card().classes(
        'w-64 min-w-64 min-h-72 p-6 shadow-md border border-gray-200 rounded-2xl flex-shrink-0'
    ):

        title_label = ui.label(
            title
        ).classes(
            'text-xl font-bold text-gray-900'
        )

        description_label = ui.label(
            description
        ).classes(
            'text-gray-600 mt-3 leading-relaxed'
        )

        warning_title_label = ui.label(
            'Warning signs'
        ).classes(
            'font-semibold text-gray-800 mt-5'
        )

        warning_signs_label = ui.label(
            warning_signs
        ).classes(
            'text-sm text-gray-600 mt-1 leading-relaxed'
        )

        learn_more_button = ui.button(
            'Learn more'
        ).props(
            'flat'
        ).classes(
            'mt-auto'
        )

        learn_more_button.on(
    'click',
    lambda: ui.notify(
        details,
        type='info'
    )
)

    return {
        'title': title_label,
        'description': description_label,
        'warning_title': warning_title_label,
        'warning_signs': warning_signs_label,
        'learn_more': learn_more_button
    }


with ui.row().classes(
    'w-full justify-center gap-4 mt-10 flex-nowrap overflow-x-auto'
).style(
    'display: flex; flex-direction: row; flex-wrap: nowrap;'
):

    banking_card = create_scam_card(
        'Banking Scams',
        'Fake bank messages, calls, and requests for financial information.',
        'OTP requests, urgent account warnings, or requests for banking details.',
        'Scammers may pretend to be your bank and create urgency to make you act quickly.'
    )

    phishing_card = create_scam_card(
        'Phishing',
        'Fake emails and websites designed to steal information.',
        'Suspicious links, fake login pages, or requests for passwords.',
        'Phishing attempts often imitate trusted companies or services.'
    )

    delivery_card = create_scam_card(
        'Delivery Scams',
        'Fake courier messages asking you to pay or verify information.',
        'Unexpected payment requests, delivery problems, or suspicious links.',
        'A scammer may claim that a delivery is delayed or requires an additional payment.'
    )

    investment_card = create_scam_card(
        'Investment Scams',
        'Fraudulent investment opportunities promising unrealistic returns.',
        'Promises of unusually high returns, pressure to invest quickly, or requests to transfer money.',
        'Investment scams may promise unusually high or guaranteed returns.'
    )

# --------------------------------------------------
# Message checker
# --------------------------------------------------

with ui.column().props(
    'id=message-checker'
).classes(
    'w-full items-center py-20 px-6 bg-gray-50'
):

    checker_title = ui.label(
    'Check a suspicious message'
).classes(
    'text-3xl font-bold text-gray-900'
)

    checker_description = ui.label(
    'Paste a message below and ScamShield will look for common warning signs.'
).classes(
    'text-lg text-gray-600 text-center mt-3 max-w-2xl'
)

    message_input = ui.textarea(
    label='Message',
    placeholder='Paste a message here...'
    ).classes(
        'w-full max-w-2xl mt-8'
    )

with ui.card().classes(
    'w-full max-w-2xl mt-6 p-6 shadow-sm'
):

    result_label = ui.label(
        'Your results will appear here.'
    ).classes(
        'text-lg font-semibold text-center w-full text-gray-500'
    )
ui.label(
    'ScamShield identifies common warning signs. '
    'It cannot guarantee that a message is safe or fraudulent.'
).classes(
    'text-sm text-gray-500 text-center max-w-2xl mt-3'
)

def check_message():

    message = message_input.value.strip().lower()

    selected = translations[
        language_selector.value
    ]

    if not message:
        result_label.set_text(
            selected['empty_message_notification']
        )

        ui.notify(
            selected['empty_message_notification'],
            type='warning'
        )

        return

    warning_signs = []

    if 'otp' in message:
        warning_signs.append('OTP request')

    if (
        'urgent' in message
        or 'immediately' in message
        or 'act now' in message
        or 'final warning' in message
    ):
        warning_signs.append(
            'Urgent or pressuring language'
        )

    if (
        'pay now' in message
        or 'payment' in message
        or 'transfer money' in message
        or 'send money' in message
        or 'gift card' in message
        or 'crypto' in message
    ):
        warning_signs.append(
            'Potential payment request'
        )

    if (
        'you won' in message
        or 'congratulations' in message
        or 'prize' in message
        or 'reward' in message
    ):
        warning_signs.append(
            'Unexpected prize or reward'
        )

    if (
        'account suspended' in message
        or 'account blocked' in message
        or 'account will be closed' in message
        or 'verify your account' in message
    ):
        warning_signs.append(
            'Account suspension or verification threat'
        )

    if (
        'call us' in message
        or 'call now' in message
        or 'call this number' in message
        or 'contact us immediately' in message
    ):
        warning_signs.append(
            'Urgent request to contact an unknown number'
        )

    if (
        'http://' in message
        or 'https://' in message
        or 'www.' in message
    ):
        warning_signs.append(
            'Web link'
        )

    if (
        'password' in message
        or 'pin' in message
        or 'card number' in message
        or 'bank details' in message
        or 'verification code' in message
    ):
        warning_signs.append(
            'Sensitive information request'
        )

    if (
        'bank' in message
        or 'police' in message
        or 'government' in message
        or 'delivery' in message
        or 'customer support' in message
        or 'security team' in message
    ):
        warning_signs.append(
            'Possible impersonation'
        )

    if warning_signs:

        if len(warning_signs) >= 3:
            risk_level = selected['risk_high']
        else:
            risk_level = selected['risk_caution']

        result_text = (
            risk_level
            + '\n\n'
            + selected['warning_signs_found']
            + ': '
            + str(len(warning_signs))
            + '\n\n'
            + selected['warning_signs_detected']
            + ':\n\n'
        )

        for warning in warning_signs:

            translated_warning = warning

            if warning == 'OTP request':
                translated_warning = selected['otp_request']

            elif warning == 'Urgent or pressuring language':
                translated_warning = selected['urgent_language']

            elif warning == 'Potential payment request':
                translated_warning = selected['payment_request']

            elif warning == 'Unexpected prize or reward':
                translated_warning = selected['unexpected_prize']

            elif warning == 'Account suspension or verification threat':
                translated_warning = selected['account_threat']

            elif warning == 'Urgent request to contact an unknown number':
                translated_warning = selected['unknown_number']

            elif warning == 'Web link':
                translated_warning = selected['web_link']

            elif warning == 'Sensitive information request':
                translated_warning = selected['sensitive_info']

            elif warning == 'Possible impersonation':
                translated_warning = selected['impersonation']

            result_text += (
                '• '
                + translated_warning
                + '\n'
            )

        result_text += (
            '\n'
            + selected['what_you_should_do']
            + ':\n\n'
            + '• '
            + selected['do_not_share']
            + '\n'
            + '• '
            + selected['do_not_click']
            + '\n'
            + '• '
            + selected['verify_message']
        )

        result_label.set_text(
            result_text
        )

        ui.notify(
            selected['warning_detected_notification'],
            type='negative'
        )

    else:

        result_label.set_text(
            selected['risk_low']
            + '\n\n'
            + selected['no_warning_signs']
            + '\n\n'
            + selected['not_guarantee_safe']
        )

        ui.notify(
            selected['no_warning_notification'],
            type='positive'
        )

    
with ui.row().classes('gap-4 mt-6'):
    
    ui.button(
    'Report a Scam'
).props(
    'outline'
).on(
    'click',
    lambda: ui.run_javascript(
        "document.getElementById('report-scam').scrollIntoView({behavior: 'smooth'});"
    )
).classes(
    'px-8 py-3'
)
    checker_button = ui.button(
    'Check Message',
    on_click=check_message
        ).props(
        'unelevated'
    ).classes(
        'px-8 py-3'
    )

    def clear_message():

        message_input.value = ''

        result_label.set_text(
            'Your results will appear here.'
        )

    ui.button(
        'Clear',
        on_click=clear_message
    ).props(
        'outline'
    ).classes(
        'px-8 py-3'
    )
    # --------------------------------------------------
# How the checker works
# --------------------------------------------------

with ui.column().classes(
    'w-full items-center py-16 px-6'
):

    ui.label(
        'How the checker works'
    ).classes(
        'text-3xl font-bold text-gray-900'
    )

    ui.label(
        'ScamShield looks for common warning signs found in scam messages.'
    ).classes(
        'text-lg text-gray-600 text-center mt-3 max-w-2xl'
    )

    with ui.row().classes(
        'w-full justify-center gap-6 mt-10 flex-wrap'
    ):

        with ui.card().classes(
            'w-64 p-6 shadow-sm'
        ):

            ui.label(
                '1. Analyze'
            ).classes(
                'text-xl font-bold text-gray-900'
            )

            ui.label(
                'The message is checked for common scam-related patterns.'
            ).classes(
                'text-gray-600 mt-3 leading-relaxed'
            )

        with ui.card().classes(
            'w-64 p-6 shadow-sm'
        ):

            ui.label(
                '2. Identify'
            ).classes(
                'text-xl font-bold text-gray-900'
            )

            ui.label(
                'Potential warning signs such as urgency, payment requests, and sensitive information requests are identified.'
            ).classes(
                'text-gray-600 mt-3 leading-relaxed'
            )

        with ui.card().classes(
            'w-64 p-6 shadow-sm'
        ):

            ui.label(
                '3. Inform'
            ).classes(
                'text-xl font-bold text-gray-900'
            )

            ui.label(
                'The results help users understand what they should be careful about.'
            ).classes(
                'text-gray-600 mt-3 leading-relaxed'
            )
            # --------------------------------------------------
# Common scam examples
# --------------------------------------------------

with ui.column().classes(
    'w-full items-center py-20 px-6 bg-gray-50'
):

    ui.label(
        'Common scam examples'
    ).classes(
        'text-3xl font-bold text-gray-900'
    )

    ui.label(
        'Learn to recognize common patterns before interacting with a suspicious message.'
    ).classes(
        'text-lg text-gray-600 text-center mt-3 max-w-2xl'
    )

    with ui.row().classes(
        'w-full justify-center gap-4 mt-10 flex-nowrap overflow-x-auto'
    ):

        with ui.card().classes(
            'w-64 min-w-64 min-h-64 p-6 shadow-md border border-gray-200 rounded-2xl flex-shrink-0'
        ):

            ui.label(
                'Banking scam'
            ).classes(
                'text-xl font-bold text-gray-900'
            )

            ui.label(
                'Example message'
            ).classes(
                'font-semibold text-gray-800 mt-5'
            )

            ui.label(
                '“Your bank account requires immediate verification. Please provide your OTP.”'
            ).classes(
                'text-gray-600 mt-2 leading-relaxed'
            )

            ui.label(
                'Warning signs: urgency, OTP request, bank impersonation.'
            ).classes(
                'text-sm text-gray-500 mt-4 leading-relaxed'
            )

        with ui.card().classes(
            'w-64 min-w-64 min-h-64 p-6 shadow-md border border-gray-200 rounded-2xl flex-shrink-0'
        ):

            ui.label(
                'Delivery scam'
            ).classes(
                'text-xl font-bold text-gray-900'
            )

            ui.label(
                'Example message'
            ).classes(
                'font-semibold text-gray-800 mt-5'
            )

            ui.label(
                '“Your package could not be delivered. Pay a small fee using the link below.”'
            ).classes(
                'text-gray-600 mt-2 leading-relaxed'
            )

            ui.label(
                'Warning signs: unexpected payment, suspicious link, delivery problem.'
            ).classes(
                'text-sm text-gray-500 mt-4 leading-relaxed'
            )

        with ui.card().classes(
            'w-64 min-w-64 min-h-64 p-6 shadow-md border border-gray-200 rounded-2xl flex-shrink-0'
        ):

            ui.label(
                'Investment scam'
            ).classes(
                'text-xl font-bold text-gray-900'
            )

            ui.label(
                'Example message'
            ).classes(
                'font-semibold text-gray-800 mt-5'
            )

            ui.label(
                '“Invest today and receive guaranteed high returns. This opportunity expires soon.”'
            ).classes(
                'text-gray-600 mt-2 leading-relaxed'
            )

            ui.label(
                'Warning signs: unrealistic returns, urgency, pressure to invest.'
            ).classes(
                'text-sm text-gray-500 mt-4 leading-relaxed'
            )

        with ui.card().classes(
            'w-64 min-w-64 min-h-64 p-6 shadow-md border border-gray-200 rounded-2xl flex-shrink-0'
        ):

            ui.label(
                'Customer support scam'
            ).classes(
                'text-xl font-bold text-gray-900'
            )

            ui.label(
                'Example message'
            ).classes(
                'font-semibold text-gray-800 mt-5'
            )

            ui.label(
                '“Your account has a problem. Contact our support team immediately to avoid suspension.”'
            ).classes(
                'text-gray-600 mt-2 leading-relaxed'
            )

            ui.label(
                'Warning signs: impersonation, urgency, unexpected contact.'
            ).classes(
                'text-sm text-gray-500 mt-4 leading-relaxed'
            )

with ui.column().props(
    'id=scam-alerts'
).classes(
    'w-full items-center py-20 px-6'
):
    ui.label(
        'Latest scam alerts'
    ).classes(
        'text-3xl font-bold text-gray-900'
    )

    ui.label(
        'Stay informed about common scam patterns and warning signs.'
    ).classes(
        'text-lg text-gray-600 text-center mt-3 max-w-2xl'
    )

    category_filter = ui.select(
        [
            'All',
            'Banking',
            'Delivery',
            'Investment',
            'Customer Support'
        ],
        value='All',
        label='Filter by category'
    ).classes(
        'w-72 mt-8'
    )

    severity_filter = ui.select(
    [
        'All',
        'High',
        'Medium'
    ],
    value='All',
    label='Filter by severity'
).classes(
    'w-72 mt-4'
)

    alert_search = ui.input(
    label='Search scam alerts',
    placeholder='Search by keyword...'
).classes(
    'w-72 mt-4'
)

    alerts_container = ui.column().classes(
    'w-full max-w-4xl gap-4 mt-10 items-stretch'
)

    def show_alerts():

        alerts_container.clear()
        found_alerts = False

        selected_category = category_filter.value
        selected_severity = severity_filter.value
        search_text = alert_search.value.strip().lower()

        with alerts_container:

            for alert in scam_alerts:

                if (
                    selected_category != 'All'
                    and alert['category'] != selected_category
                ):
                    continue

                if (
                    selected_severity != 'All'
                    and alert['severity'] != selected_severity
                ):
                    continue

                search_content = (
                    alert['title']
                    + ' '
                    + alert['category']
                    + ' '
                    + alert['description']
                    + ' '
                    + alert['warning_signs']
                ).lower()

                if search_text and search_text not in search_content:
                    continue

                found_alerts = True

                with ui.card().classes(
    'w-full p-7 shadow-md border border-gray-200 rounded-2xl'
):

                    ui.label(
                        alert['title']
                    ).classes(
                        'text-xl font-bold text-gray-900'
                    )

                    ui.label(
                        alert['description']
                    ).classes(
                        'text-gray-600 mt-3'
                    )

                            #category

                    ui.label(
                        'Category: ' + alert['category']
                    ).classes(
                        'text-sm text-gray-500 mt-4'
                    )
                    
                    #severity 
                    
                    severity_class = (
                        'bg-red-100 text-red-700'
                        if alert['severity'] == 'High'
                        else 'bg-orange-100 text-orange-700'
                    )

                    ui.label(
                        'Severity: ' + alert['severity']
                    ).classes(
                        severity_class
                        + ' px-3 py-1 rounded-full text-sm font-semibold mt-3'
                    )
                    
                    #Warning signs and actions
                    
                    with ui.column().classes(
                        'w-full mt-5 p-4 bg-gray-50 rounded-xl'
                    ):

                        ui.label(
                            'Warning signs'
                        ).classes(
                            'font-semibold text-gray-800'
                        )

                        ui.label(
                            alert['warning_signs']
                        ).classes(
                            'text-sm text-gray-600 mt-1'
                        )

                    #what to do

                    with ui.column().classes(
                        'w-full mt-4 p-4 bg-blue-50 rounded-xl'
                    ):

                        ui.label(
                            'What to do'
                        ).classes(
                            'font-semibold text-gray-800'
                        )

                        ui.label(
                            alert['action']
                        ).classes(
                            'text-sm text-gray-700 mt-1 leading-relaxed'
                        )

        if not found_alerts:

            ui.label(
                'No scam alerts found.'
            ).classes(
                'text-lg text-gray-600 text-center w-full py-8'
            )

show_alerts()

category_filter.on_value_change(
    lambda: show_alerts()
)

severity_filter.on_value_change(
    lambda: show_alerts()
)

alert_search.on_value_change(
    lambda: show_alerts()
)

# --------------------------------------------------
# Learn
# --------------------------------------------------

with ui.column().props(
    'id=learn'
).classes(
    'w-full items-center py-20 px-6 bg-gray-50'
):

    ui.label(
        'Learn how to stay safe'
    ).classes(
        'text-3xl font-bold text-gray-900'
    )

    ui.label(
        'Simple guidance to help you recognize scams and protect yourself online.'
    ).classes(
        'text-lg text-gray-600 text-center mt-3 max-w-2xl'
    )

    with ui.row().classes(
    'w-full justify-center gap-3 mt-10 flex-nowrap overflow-x-auto'
):

        with ui.card().classes(
            'w-80 p-6 shadow-sm border border-gray-200 rounded-xl'
        ):

            ui.label(
                'Recognize warning signs'
            ).classes(
                'text-xl font-bold text-gray-900'
            )

            ui.label(
                'Be careful when a message creates urgency, asks for money, '
                'requests sensitive information, or contains a suspicious link.'
            ).classes(
                'text-gray-600 mt-3 leading-relaxed'
            )

        with ui.card().classes(
            'w-80 p-6 shadow-sm'
        ):

            ui.label(
                'Protect your information'
            ).classes(
                'text-xl font-bold text-gray-900'
            )

            ui.label(
                'Never share passwords, PINs, OTPs, or other sensitive banking '
                'information with someone who contacts you unexpectedly.'
            ).classes(
                'text-gray-600 mt-3 leading-relaxed'
            )

        with ui.card().classes(
            'w-80 p-6 shadow-sm'
        ):

            ui.label(
                'Verify before acting'
            ).classes(
                'text-xl font-bold text-gray-900'
            )

            ui.label(
                'If a message claims to come from a bank, company, or government '
                'organization, verify it using an official source before taking action.'
            ).classes(
                'text-gray-600 mt-3 leading-relaxed'
            )

        with ui.card().classes(
            'w-80 p-6 shadow-sm'
        ):

            ui.label(
                'If something feels suspicious'
            ).classes(
                'text-xl font-bold text-gray-900'
            )

            ui.label(
                'Do not rush. Stop, verify the information, and consider reporting '
                'the suspicious activity through an appropriate official channel.'
            ).classes(
                'text-gray-600 mt-3 leading-relaxed'
            )
            # --------------------------------------------------
# Report a scam
# --------------------------------------------------

with ui.column().props(
    'id=report-scam'
).classes(
    'w-full items-center py-20 px-6'
):

    ui.label(
        'Report a scam'
    ).classes(
        'text-3xl font-bold text-gray-900'
    )

    ui.label(
        'If you believe you have encountered a scam, take a moment to stop, '
        'verify the information, and report it through an appropriate official channel.'
    ).classes(
        'text-lg text-gray-600 text-center mt-3 max-w-2xl'
    )

    with ui.card().classes(
        'w-full max-w-2xl p-8 mt-10 shadow-sm'
    ):

        ui.label(
            'Before reporting'
        ).classes(
            'text-xl font-bold text-gray-900'
        )

        ui.label(
            'Do not share passwords, PINs, OTPs, card details, or other sensitive '
            'information with ScamShield.'
        ).classes(
            'text-gray-600 mt-3 leading-relaxed'
        )

        ui.label(
            'For users in Dubai, use the official Dubai Police cybercrime reporting '
            'service for appropriate reports.'
        ).classes(
            'text-gray-600 mt-3 leading-relaxed'
        )

        ui.link(
            'Visit Dubai Police cybercrime services',
            'https://www.dubaipolice.gov.ae/'
        ).classes(
            'text-primary font-semibold mt-6'
        )
# --------------------------------------------------
# Footer
# --------------------------------------------------

with ui.footer().classes(
    'bg-gray-900 text-white py-8'
):

    with ui.column().classes(
        'w-full items-center'
    ):

        ui.label(
            'ScamShield'
        ).classes(
            'text-xl font-bold'
        )

        ui.label(
            'Helping communities recognize and respond to scams.'
        ).classes(
            'text-gray-300 mt-2'
        )


# --------------------------------------------------
# Start application
# --------------------------------------------------

ui.run()