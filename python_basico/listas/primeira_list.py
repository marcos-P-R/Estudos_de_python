languages = ['JS', 'Java', 'Python', 'TypeScript']
new_languages = ['C#', 'Rust']

print(languages[3].upper())
languages.append('Golang')
languages.append('Kotlin')
languages.insert(1, 'Lua')
print(languages)
languages.reverse()
print(languages)
languages[0: 1] = new_languages
print(languages)
