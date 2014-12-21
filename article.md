One key goal of a successful devops process - and successful usage of AWS - is to create automated, repeatable processes. It may be acceptable to spin up EC2 instances by hand in the early stage of a project, but it's important to convert this from a manual experiment to a fully described system before the project reaches production.

There are several great tools to describe the configuration of a single instance- Ansible, Chef, Puppet, Salt- but these tools aren't well-suited for describing the configuration of an entire system. This is where Amazon's CloudFormation comes in.

CloudFormation was launched in 2011. It's fairly daunting to get started with, errors in CloudFormation templates are typically not caught until late in the process, and since it is fed by JSON files it's easy to make mistakes. Proper JSON is unwieldy (stray commas, unmatched closing blocks), but it's fairly easy to write YAML and convert it to JSON.

Let's start with a simple CloudFormation template to create an EC2 instance. In this example many things are hardcoded, like the instance type and AMI. This cuts down on the complexity of the example. Still, it's a nontrivial example that creates a VPC and other resources. The only prerequisite for this example is to create a keypair in the US-West-2 region called "advent2014".

JSON:

#include simple-ec2.json

As you look at this template, notice both the quirks of CloudFormation (especially "Ref" and "Fn::GetAtt") and the quirks of JSON. Even with some indentation the brackets are complex, and correct comma placement is difficult while editing a template.

Next, let's convert this JSON example to YAML. [There's a quick converter in this article's repository](https://github.com/tedder/aws-advent-2014-yml-cloudformation/json-to-yaml.py), with python and pip installed, the only other dependency should be to install PyYAML with pip.

Since JSON doesn't maintain position of hashes/dicts, the output order may vary. Here's what it looks like immediately after conversion:

#include simple-ec2.yml
