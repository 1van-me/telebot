from google_drive_downloader import GoogleDriveDownloader as gdd
answer=input("Введите команду")
if answer=="скачать":
    gdd.download_file_from_google_drive(file_id='https://drive.google.com/open?id=1aKfwJKh0B2Vhe6H-h08RwU_3XC1qFdW2',
                                    dest_path='',
                                   