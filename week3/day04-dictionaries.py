# Lesson
# A dict stores key-value pairs: {'name': 'web-01', 'status': 'running'}. Access values by key, add new keys by assignment, check membership with 'in'.

# Challenge — write this as a script
# Write a script representing an EC2 instance as a dict with keys id, type, region, and status. Print a formatted summary line, then update status to 'stopped' and print the updated dict.

ec2_instance = {
    "id": "ami-960522",
    "type"   : "t3.medium",
    "region" : "ap-northeast-1",
    "status" : "running"
}
print(f"AMI: {ec2_instance.get("id")} \nInstance Type: {ec2_instance.get("type")} \nRegion: {ec2_instance.get("region")} \nStatus: {ec2_instance.get("status")}")
ec2_instance.update({"status": "stopped"})
print(ec2_instance)