import os

extensions_to_normal_name = {
        'py': 'Python',
        'rs': 'Rust',
        'sh': 'Bash',
        'cpp': 'C++',
        'hs': 'Haskell',
        'java': 'Java'
}

def get_extension(filename: str) -> str:
    if filename.find('.') == -1:
        return ''

    return filename.split('.')[1]
def count_extensions(extensions) -> dict:
    result = {}
    for extension in extensions:
        if extension in result:
            result[extension] += 1
        else:
            result[extension] = 1

    return result

def convert_to_markdown(counted_extensions: dict) -> str:
    total = 0

    result = '| Language: | Problems solved: |\n'
    result += '| --------- | ---------------- |\n'

    for language in counted_extensions:
        count = counted_extensions[language]
        result += f'| {language} | {count} |\n'
        total += count
    
    result += f'| **Total:** | {total} |\n'

    return result

if __name__ == "__main__":
    dirs_to_ignore = ['./.git']
    extensions_to_ignore = ['txt', '']
    all_files = [files for dirname, subdirs, files in os.walk('.') if not any(dir_pattern in dirname for dir_pattern in dirs_to_ignore)][1:]

    all_files = sum(all_files, [])
    all_extensions = [get_extension(filename) for filename in all_files]

    all_code_extensions = [extensions_to_normal_name[extension] for extension in all_extensions if extension not in extensions_to_ignore]

    counted_extensions = count_extensions(all_code_extensions)
    markdown = convert_to_markdown(counted_extensions)

    with open('README.md', 'r+') as fp:
        line = fp.readline()

        while line != '## Languages used:\n':
            line = fp.readline()
        
        fp.seek(fp.tell())
        fp.write(markdown)
