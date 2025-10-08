resource "aws_s3_bucket" "demo" {
  bucket = "public-demo-bucket"
  acl    = "public-read" 
}
