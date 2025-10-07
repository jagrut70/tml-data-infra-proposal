terraform {
  required_version = ">= 1.6.0"
}

provider "aws" {
  region = var.region
}

variable "region" {
  type    = string
  default = "us-east-1"
}

output "note" {
  value = "Replace with your cloud and modules"
}
