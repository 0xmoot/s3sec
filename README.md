# s3sec

Test AWS S3 buckets for read/write/delete access

This tool was developed to quickly test a list of s3 buckets for public read, write and delete access for the purposes of penetration testing on bug bounty programs.

![Screenshot](https://0xmoot.com/git/screenshots/s3sec2.png)

Found a bug bounty using this tool? 
Feel free to add me as a collaborator: [@0xmoot](https://0xmoot.com) :)

## Installation

Clone the git repo onto your machine:

```bash
git clone https://github.com/0xmoot/s3sec
```

Happy hunting :)

## Usage

Check a single S3 instance:

```bash
echo "test-instance.s3.amazonaws.com" | python3 s3sec.py
```

Or:

```bash
echo "test-instance" | python3 s3sec.py
```

Check a list of S3 instances:

```bash
cat locations | python3 s3sec.py
```


## Setup AWS CLI & Credentials (optional)

To get the most out of this tool you should install the AWS CLI and setup user credentials. 

With AWS CLI a series of deeper tests (including unsigned read, writing files and deleting files) is activated:

#### Installing AWS CLI on Kali Linux

To install AWS CLI you can simply install using below command:

```bash
pip3 install awscli
```

#### Getting AWS Credentials (Access Key ID and AWS Secret Access Key)

1. Sign up for Amazon's AWS from their official website: [https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc)

2. Login into your AWS account and click on My Security Credentials.

3. Click on Access Keys (access key id and secret access key) to get your login credentials for AWS CLI.

4. Then click on Show Access Key option to get your Access Key ID and Secret Access Key or you can download it as well.

#### Configuring AWS CLI on Kali Linux

1. Start a terminal and enter the below commands then enter the AWS Access Key ID and AWS Secret Access Key that was created in previous steps.

```bash
aws configure
```

Use the following default settings:

```text
AWS Access Key Id: <<Your Key>>
AWS Secret Access Key: <<Your Secret Access Key>>
Default region name: ap-south-1
Default output format: json
```

## Disclaimer
The developers assume no liability and are not responsible for any misuse or damage caused by the s3sec tool. The tool is provided as-is for educational and bug bounty purposes.

## License
[MIT License](https://choosealicense.com/licenses/mit/)