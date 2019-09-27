# Create File Github Action

**Name: jdharms/create-file@v1**

Github Action to create a .env file with Github Secrets

## Usage

This action creates a file in the Job's working directory, probably for purposes of deployment.  The use-case that inspired this Action is writing out a private/public
key pair to the file system that can be deployed alongside a Google App Engine deploy action, keeping the private key in Github's Secret store.

Exactly two input values are expected, `file_name` and `file_contents`.

```
name: Create File
on: push

jobs:
  create-file:
    runs-on: ubuntu-18.04
    steps:
    - name: Create RSA Private Key File
      uses: jdharms/create-file@v1
      with:
        file_name: 'backend/jwtRS256.key'
        file_contents: ${{ secrets.JWT_PRIV_KEY }}
```

In this example, the file `backend/jwtRS256.key` will be created with the value of `file_contents` as its contents.

For v1, the file will be created with the exact value of `file_contents`.  v2 is planned to decode base64 strings into `file_name`.
