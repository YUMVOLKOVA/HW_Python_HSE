def generate_table(data):
    number_of_elements = True
    for row in range(len(data)):
        if len(data[row]) != len(data[0]):
            number_of_elements = False
            break
    if not number_of_elements:
        raise Exception('different length of lines')

    for row in range(len(data)):
        for column in range(len(data[0])):
            data[row][column] = str(data[row][column])

    start_document = '\documentclass{article}\n\\begin{document}\n'

    start_table = '''\\begin{table}[h!]\n'''
    line_breaks = '\\begin{tabular}{|' + 'c|' * len(data[0]) + '}\n\hline\n'
    headers = ''
    for i in range(len(data[0])):
        if '_' in data[0][i]:
            tmp = data[0][i].split('_')
            headers = headers + '\\textbf{' + tmp[0] + '\_' + tmp[1] + '}'
        else:
            headers = headers + '\\textbf{' + data[0][i] + '}'
        if i != len(data[0]) - 1:
            headers += ' & '
        else:
            headers += ' \\\\ \hline\n'

    table = ''.join(map(lambda row: ' & '.join(row) + ' \\\\ \hline\n', data[1:]))

    end_table = '\n\end{tabular}\n\end{table}\n'
    end_document = '\end{document}\n'

    full_document = start_document + \
                    start_table + \
                    line_breaks + \
                    headers +\
                    table + \
                    end_table + \
                    end_document

    # save table into artifacts
    with open('artifacts/easy.tex', 'w', encoding="utf-8") as file:
        file.write(full_document)


if __name__ == '__main__':
    list_of_lists = [['name', 'japanese_name', 'classification', 'type1', 'type2', 'abilities'],
                     ['Bulbasaur', 'Fushigidaneフシギダネ', 'Seed Pokémon', 'grass', 'poison', 'Chlorophyll, Overgrow'],
                     ['Ivysaur', 'Fushigisouフシギソウ', 'Seed Pokémon', 'grass', 'poison', 'Chlorophyll, Overgrow'],
                     ['Venusaur', 'Fushigibanaフシギバナ', 'Seed Pokémon', 'grass', 'poison', 'Chlorophyll, Overgrow'],
                     ['Charmander', 'Hitokageヒトカゲ', 'Lizard Pokémon', 'fire', '-', 'Solar Power, Blaze'],
                     ['Charmeleon', 'Lizardoリザード', 'Flame Pokémon', 'fire', '-', 'Solar Power, Blaze'],
                     ['Charizard', 'Lizardonリザードン', 'Flame Pokémon', 'fire', 'flying', 'Solar Power, Blaze'],
                     ['Squirtle', 'Zenigameゼニガメ', 'Tiny Turtle Pokémon', 'water', '-', 'Rain Dish, Torrent'],
                     ['Wartortle', 'Kameilカメール', 'Turtle Pokémon', 'water', '-', 'Rain Dish, Torrent'],
                     ['Blastoise', 'Kamexカメックス', 'Shellfish Pokémon', 'water', '-', 'Rain Dish, Torrent'],
                     ['Caterpie', 'Caterpieキャタピー', 'Worm Pokémon', 'bug', '-', 'Run Away, Shield Dust']]

    generate_table(list_of_lists)
