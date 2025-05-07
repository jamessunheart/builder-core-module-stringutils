def reverse_string(text):
    return text[::-1]

def capitalize_words(text):
    return ' '.join(word.capitalize() for word in text.split())

def run(params):
    action = params.get('action', 'reverse')
    text = params.get('text', '')
    if action == 'reverse':
        return {'result': reverse_string(text)}
    elif action == 'capitalize':
        return {'result': capitalize_words(text)}
    else:
        return {'error': 'Invalid action specified'}