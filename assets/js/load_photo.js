
class Observable {
    _valueChangedCallback = null;
    onChange(callback) {
        this._valueChangedCallback = callback;
    }
    raiseChangedEvent(value) {
        if (this._valueChangedCallback) {
            this._valueChangedCallback(value);
        }
    };
}
class ImagePreview extends Observable {
    _value = null;
    set value(_value) {
        if (this._value != _value) {
            this._value = _value;
            this.raiseChangedEvent(_value);
        }
    }
    get value() {
        return this.value;
    }
}
const DefaultPersonImageUrl = './assets/img/avatar.jpeg';
const imagePreview = new ImagePreview(DefaultPersonImageUrl);
let imageFile = "";
let imageUrl = "";
imagePreview.onChange((value)=>{
    const $imagePreview=document.getElementById("image-preview");
    $imagePreview.src=value;
})
let invalidPhoto = {
    size: false,
    type: false,
}
let maxFileSize = 1048576 * 4; // 1MB

const onImageSelected = (event) => {
    console.log("EVENT", event);
    let input = (event.target);
    if (!input.files || !input.files.length) {
        return;
    }
    imageFile = input.files[0];

    if (imageFile) {
        let isValid = true;
        const fileType = validateFileType(imageFile, [FileTypesEnum.png, FileTypesEnum.jpg]);
        if (!fileType) {
            invalidPhoto.type = true;
            console.error("DEV - LoadPhoto - onImageSelected()\nImage File not supported")
            // messageService.add({
            //     severity: 'error',
            //     summary: `Tipo de imágen no válido`,
            //     detail: `Los tipos de imágenes .png, .jpg o .jpeg`,
            // });
        } else if (imageFile.size > maxFileSize) {
            isValid = false;
            invalidPhoto.size = true;
            console.error(`DEV - Evaluation Edit - onImageSelected()\nImage too weight. Upload images with a size greater than ${FormatFileSizePipe.transform(maxFileSize, false)}.`);
            // messageService.add({
            //     severity: 'error',
            //     summary: `Tamaño de archivo muy grande`,
            //     detail: `La imagen no debe pesar más de ${FormatFileSizePipe.transform(maxFileSize, false)}.`,
            // });
        }

        if (isValid) {
            getFileAsDataURL(imageFile).then((result) => {
                imagePreview.value = result;
            });
        } else {
            input.value = "";
            imagePreview.value = DefaultPersonImageUrl;
            imageFile = undefined;
        }
    }
}
const getFileAsDataURL = async (file) => {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => {
            resolve(reader.result);
        };
        reader.onerror = () => {
            reject(reader.error);
        }
        reader.readAsDataURL(file);
    })
}
const validateFileType = (file, allowedFileTypes) => {
    let mimeType = file.type;
    if (mimeType in FileMimeTypesEnum) {
        const fileType = MimeTypesToFileTypes[mimeType];
        if (allowedFileTypes.includes(fileType)) {
            return fileType;
        }
    }
    return undefined;
}

class FileTypesEnum {
    static 'zip' = 'zip';
    static 'rar' = 'rar';
    static 'pdf' = 'pdf';
    static 'docx' = 'docx';
    static 'xlsx' = 'xlsx';
    static 'png' = 'png';
    static 'jpg' = 'jpg';
}

const FileTypesEnumValues = Object.values(FileTypesEnum);
class FileMimeTypesEnum {
    static 'application/zip' = 'application/zip';
    static 'application/octet-stream' = 'application/octet-stream';
    static 'application/x-zip-compressed' = 'application/x-zip-compressed';
    static 'multipart/x-zip' = 'multipart/x-zip';
    static 'aplication/x-7z-compressed' = 'aplication/x-7z-compressed';
    static 'aplication/7z-compressed' = 'aplication/7z-compressed';
    static 'application/vnd.rar' = 'application/vnd.rar';
    static 'application/x-rar-compressed' = 'application/x-rar-compressed';
    static 'application/pdf' = 'application/pdf';
    static 'application/vnd.cups-pdf' = 'application/vnd.cups-pdf';
    static 'application/x-pdf' = 'application/x-pdf';
    static 'application/msword' = 'application/msword';
    static 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document';
    static 'application/vnd.openxmlformats-officedocument.wordprocessingml.template' = 'application/vnd.openxmlformats-officedocument.wordprocessingml.template';
    static 'application/vnd.ms-word.document.macroEnabled.12' = 'application/vnd.ms-word.document.macroEnabled.12';
    static 'application/vnd.ms-word.template.macroEnabled.12' = 'application/vnd.ms-word.template.macroEnabled.12';
    static 'application/vnd.ms-excel' = 'application/vnd.ms-excel';
    static 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet';
    static 'application/vnd.openxmlformats-officedocument.spreadsheetml.template' = 'application/vnd.openxmlformats-officedocument.spreadsheetml.template';
    static 'application/vnd.ms-excel.sheet.macroEnabled.12' = 'application/vnd.ms-excel.sheet.macroEnabled.12';
    static 'application/vnd.ms-excel.template.macroEnabled.12' = 'application/vnd.ms-excel.template.macroEnabled.12';
    static 'application/vnd.ms-excel.addin.macroEnabled.12' = 'application/vnd.ms-excel.addin.macroEnabled.12';
    static 'application/vnd.ms-excel.sheet.binary.macroEnabled.12' = 'application/vnd.ms-excel.sheet.binary.macroEnabled.12';
    static 'image/png' = 'image/png';
    static 'image/jpeg' = 'image/jpeg';
}
const FileMimeTypesEnumValues = Object.values(FileMimeTypesEnum);
const MimeTypesToFileTypes = {
    'application/zip': FileTypesEnum.zip,
    'application/octet-stream': FileTypesEnum.zip,
    'application/x-zip-compressed': FileTypesEnum.zip,
    'multipart/x-zip': FileTypesEnum.zip,
    'aplication/x-7z-compressed': FileTypesEnum.zip,
    'aplication/7z-compressed': FileTypesEnum.zip,
    'application/vnd.rar': FileTypesEnum.rar,
    'application/x-rar-compressed': FileTypesEnum.rar,
    'application/pdf': FileTypesEnum.pdf,
    'application/vnd.cups-pdf': FileTypesEnum.pdf,
    'application/x-pdf': FileTypesEnum.pdf,
    'application/msword': FileTypesEnum.docx,
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document': FileTypesEnum.docx,
    'application/vnd.openxmlformats-officedocument.wordprocessingml.template': FileTypesEnum.docx,
    'application/vnd.ms-word.document.macroEnabled.12': FileTypesEnum.docx,
    'application/vnd.ms-word.template.macroEnabled.12': FileTypesEnum.docx,
    'application/vnd.ms-excel': FileTypesEnum.xlsx,
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': FileTypesEnum.xlsx,
    'application/vnd.openxmlformats-officedocument.spreadsheetml.template': FileTypesEnum.xlsx,
    'application/vnd.ms-excel.sheet.macroEnabled.12': FileTypesEnum.xlsx,
    'application/vnd.ms-excel.template.macroEnabled.12': FileTypesEnum.xlsx,
    'application/vnd.ms-excel.addin.macroEnabled.12': FileTypesEnum.xlsx,
    'application/vnd.ms-excel.sheet.binary.macroEnabled.12': FileTypesEnum.xlsx,
    'image/png': FileTypesEnum.png,
    'image/jpeg': FileTypesEnum.jpg,
}
const FileTypesToMimeTypes = {
    'zip': [FileMimeTypesEnum['application/zip'], FileMimeTypesEnum['application/octet-stream'], FileMimeTypesEnum['application/x-zip-compressed'], FileMimeTypesEnum['multipart/x-zip'], FileMimeTypesEnum['aplication/x-7z-compressed'], FileMimeTypesEnum['aplication/7z-compressed'],],
    'rar': [FileMimeTypesEnum['application/vnd.rar'], FileMimeTypesEnum['application/x-rar-compressed'], FileMimeTypesEnum['application/octet-stream'],],
    'pdf': [FileMimeTypesEnum['application/pdf'], FileMimeTypesEnum['application/vnd.cups-pdf'], FileMimeTypesEnum['application/x-pdf'],],
    'docx': [FileMimeTypesEnum['application/msword'], FileMimeTypesEnum['application/vnd.openxmlformats-officedocument.wordprocessingml.document'], FileMimeTypesEnum['application/vnd.openxmlformats-officedocument.wordprocessingml.template'], FileMimeTypesEnum['application/vnd.ms-word.document.macroEnabled.12'], FileMimeTypesEnum['application/vnd.ms-word.template.macroEnabled.12'],],
    'xlsx': [FileMimeTypesEnum['application/vnd.ms-excel'], FileMimeTypesEnum['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'], FileMimeTypesEnum['application/vnd.openxmlformats-officedocument.spreadsheetml.template'], FileMimeTypesEnum['application/vnd.ms-excel.sheet.macroEnabled.12'], FileMimeTypesEnum['application/vnd.ms-excel.template.macroEnabled.12'], FileMimeTypesEnum['application/vnd.ms-excel.addin.macroEnabled.12'], FileMimeTypesEnum['application/vnd.ms-excel.sheet.binary.macroEnabled.12'],],
    'png': [FileMimeTypesEnum['image/png']],
    'jpg': [FileMimeTypesEnum['image/jpeg'],],
}

const FILE_SIZE_UNITS = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];
const FILE_SIZE_UNITS_LONG = ['Bytes', 'Kilobytes', 'Megabytes', 'Gigabytes', 'Pettabytes', 'Exabytes', 'Zettabytes', 'Yottabytes'];

class FormatFileSizePipe {
    static transform(sizeInBytes, longForm) {
        const units = longForm
            ? FILE_SIZE_UNITS_LONG
            : FILE_SIZE_UNITS;

        let power = Math.round(Math.log(sizeInBytes) / Math.log(1024));
        power = Math.min(power, units.length - 1);

        const size = sizeInBytes / Math.pow(1024, power); // size in new units
        const formattedSize = Math.round(size * 100) / 100; // keep up to 2 decimals
        const unit = units[power];

        return `${formattedSize} ${unit}`;
    }
}