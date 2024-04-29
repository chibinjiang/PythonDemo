from rembg import remove

input_path = '/Users/chibinjiang/Downloads/00_Masami_Horii.png'
output_path = 'Masami_Horri_output.png'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)
