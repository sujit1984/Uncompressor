import PySimpleGUI as sg
import extractor as ex


label1 = sg.Text("Select the archive")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select the destination")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="dest_folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("Archiver Decompressor", layout=[[label1, input1, choose_button1],
                                                [label2, input2, choose_button2],
                                                [extract_button, output_label]],
                font=("Helvetica", 14))

while True:
    event, values = window.read()
    print(event,values)
    arvhivepath = values['archive']
    #files_to_compress = filepaths.split(";")
    #print(files_to_compress)
    folder = values['dest_folder']
    ex.file_extractor(arvhivepath, folder)
    print("Zip File Extracted")
    window['output'].update(value="Extraction Completed!")

window.close()


