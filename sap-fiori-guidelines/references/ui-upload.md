# SAP Fiori UI Elements: Upload

This reference covers the following UI components:

- [File Uploader](#file-uploader)

---

## file-uploader

The file uploader lets users select one or more files using their local file explorer and upload them to the application. Uploading starts automatically as soon as users select the files.

Unlike the [upload collection](https://sap.github.io/ui5-webcomponents/components/fiori/UploadCollection/) component, the file uploader includes only an input field or button and is designed for simple upload tasks.

*File uploader with an input field*

## When to Use

Do
Use the file uploader:
- To upload one or more files using the local file
explorer.
- To upload files by dragging and dropping them.
- If users may need to rename uploaded files.
In all these cases, use the [upload collection](https://sap.github.io/ui5-webcomponents/components/fiori/UploadCollection/) component instead.

+----------------------------------------------------------x----------------------------------------------------------+
Top Tips
+----------------------------------------------------------x----------------------------------------------------------+
- The file uploader works best for uploading **single files**.
- Use the [upload collection](https://sap.github.io/ui5-webcomponents/components/fiori/UploadCollection/) component
when users need to manage multiple uploads (such as deleting individual files, rearranging files, and renaming
files).

## Anatomy

*Anatomy of the file uploader*

1. **Input:** Container field.
2. **Placeholder text:** Upload hint.
3. **Browse button:** Removes any uploaded files and
opens the file explorer dialog of the local operating
system.
## Types

The file uploader offers two options for uploading files, an input field and a button.

*File uploader types*

**A. File uploader with input field**
**B. File uploader button only**

**> **Guideline:** **

If you use the button-only variant, make sure users can see the file name after the upload finishes. This guideline
doesn’t specify how to display the file name.

## States

### Component States

The file uploader has two basic [component states](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-component-states): enabled and disabled.

*File uploader component states*

**A. Enabled**
**B. Disabled**

### Interaction States

The file uploader has three basic [interaction states](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-interaction-states) (regular, hover, down) and a busy state. For the busy state, you can also display a message with additional information below the field. 

*File uploader interaction states*

**A. Regular**
**B. Hover**
**C. Down**
**D. Busy**

### Focus States

The file uploader has three basic [focus states](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-focus-states): on focus, on focus while uploaded, and token focus.

*File uploader focus states*

**A. On focus**
**B. On focus while uploaded**
**C. Token focus**

### Value States

*File uploader value states*

The file uploader has four basic [value states](https://www.sap.com/design-system/fiori-design-web/foundations/interaction/states/interaction-foundations-value-states):

**A. Positive**
**B. Critical**
**C. Negative**
**D. Information**

For all value states, you can also display a message with additional information below the field.

## Behavior and Interaction

The upload flow depends on whether you use the file uploader with an input field or only an upload button.

### File Uploader with an Input Field

#### New Upload – Select Using File Explorer

**A. Start upload using file explorer:** The user clicks
the browse button or an empty area inside the input field.
*Upload flow with an input field using the file explorer*
**B. Select files:** The local file explorer opens in a
dialog. The user selects files to upload and confirms the
selection.
**C. Upload in progress:** While files upload, each file
token shows a busy indicator. An information message
indicates which files are being uploaded.
**D. Upload result:**
- **Success:** The uploader shows a success state in the
input field and displays a message confirming the upload.
After uploading, each token displays the file name. The
system sets the focus on the last uploaded token.
- **Error:** If there's an error – for example, when the
file size exceeds the upload limit – the component doesn't
upload the file, and no token is displayed. The input field
shows an error state and an error message. The error state
remains visible until the user uploads a new file.
- **Error when uploading multiple files:**
If one file in a batch has an error, the error message
names that file. No files are uploaded, and no tokens
appear. The user must reselect all files for upload.
#### New Upload – Select Using Drag and Drop

**A. Start upload using drag and drop**: The user drops the file(s) into the input field.
**B. Upload in progress:** While files upload, each file token shows a busy indicator. An
information message indicates which files are being uploaded.
**C. Upload result:**
- **Success:** The uploader shows a success state in the input field and displays a
message confirming the upload. After uploading, each token displays the file name. The
system sets the focus on the last uploaded token.
- **Error:** If there's an error – for example, when the file size exceeds the upload
limit – the component doesn't upload the file, and no token is displayed. The input field
shows an error state and an error message. The error state remains visible until the user
uploads a new file.
- **Error when uploading multiple files:**
If one file in a batch has an error, the error message names that file. No files are
uploaded, and no tokens appear. The user must reselect all files for upload.
#### Uploading Files When the File Uploader Is Busy

**A. Files are uploading**
**B. Restart upload:** To start a new upload, the user
clicks the browse button or an empty area inside the
input field.
**C. Select new files:** A dialog opens with the local
file explorer. The user picks new files and confirms the
selection.
**D. Upload complete:** Each successfully uploaded file
appears as a token. The focus moves to the last token.
#### Replacing Files

The user must replace all existing files when making a
new selection. Adding files to the current selection
isn't possible. The uploader replaces the files and
uploads the newly selected files.
**A. Start upload:** To start a new upload, the user
clicks the browse button or an empty area inside the
input field.
**B. Select new files:** A dialog opens with the local
file explorer. The user picks new files and confirms the
selection.
**C. Upload in progress:** While files upload, each file
token shows a busy indicator.
**D. Upload complete:** Each successfully uploaded file
appears as a token. The focus moves to the last token.
#### Removing Uploaded Files

*Removing all uploaded files*

**A. Uploaded files:** Previously uploaded files display as tokens in the input field.
**B. Remove all files:** Clicking the *Remove All Files* button removes all uploaded files. This button appears only when uploaded files are present.
**C: Cleared field:** Users can upload new files by starting the upload process again.

#### Truncation

File names on tokens are truncated when there isn't enough space.

If the tokens don’t all fit in the input field, the component shows an overflow button (with "n more" or "n items"). For more information, see [Multi Input](https://www.sap.com/design-system/fiori-design-web/ui-elements/multi-input-web-component/).

*Truncation in the file uploader*

**A. Truncated placeholder text**
**B. Single file with truncated token text**
**C. Multiple files –** ***n more*****overflow button:** At least one file name appears as a token in the input field next to the "n more" button.

### File Uploader with an Upload Button

**A. Start upload:** The user clicks the upload button

**B. Select files:** The local file explorer opens in a
dialog. The user selects files to upload and confirms the
selection.
**> **Guideline:** **

Display the uploaded files next to the file uploader button. Users must always be able to see which files have
already been uploaded.

## Localization

File uploader supports left-to-right (LTR) and right-to-left (RTL) reading directions.

*File uploader in left-to-right mode*

---

