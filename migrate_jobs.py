import os
import subprocess
import xml.etree.ElementTree as ET

def export_jenkins_job(job_name):
    command = ["jenkins-jobs", "export", "job-templates", job_name]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout

def import_to_cloudbees(config_xml):
    command = ["jenkins-jobs", "update", "-"]
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate(input=config_xml)
    return stdout, stderr

def main():
    job_names = ["job1", "job2"]  # List of job names to migrate
    
    for job_name in job_names:
        print(f"Exporting {job_name} from Jenkins...")
        job_config = export_jenkins_job(job_name)
        
        print(f"Migrating {job_name} to CloudBees Jenkins...")
        stdout, stderr = import_to_cloudbees(job_config)
        
        if stderr:
            print(f"Error migrating {job_name}: {stderr.decode('utf-8')}")
        else:
            print(f"{job_name} migrated successfully!")

if __name__ == "__main__":
    main()
