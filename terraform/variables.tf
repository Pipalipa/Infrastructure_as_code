variable "vpc_cidr" {
  default = "10.0.0.0/16"
}

variable "public_subnet_cidr" {
  default = "10.0.1.0/24"
}

variable "availability_zone" {
  default = "us-east-1a"
}

variable "web_ami" {
  default = "ami-01fccab91b456acc2"
}

variable "db_ami" {
  default = "ami-01fccab91b456acc2"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "key_name" {
  default = "project_cloud"
}

variable "private_key_path" {
  description = "The path to the private key file"
  default     = "~/.ssh/project_cloud.pem"
}
