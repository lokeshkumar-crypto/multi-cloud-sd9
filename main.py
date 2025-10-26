def main():
    with open('input.txt') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    project_title = lines[0]
    project_id = lines[1]
    cloud_platforms = lines[2:5]
    advantages = lines[5]
    challenges = lines[6]
    
    report = []
    report.append(f"Project Title: {project_title}")
    report.append(f"Project ID: {project_id}")
    report.append("Cloud Platforms Used: " + ", ".join(cloud_platforms))
    report.append("Advantages:" + advantages.split(":",1)[-1].strip())
    report.append("Challenges:" + challenges.split(":",1)[-1].strip())
    
    with open('output.txt', 'w') as out:
        for line in report:
            print(line)      # Show in workflow logs
            out.write(line + '\n')  # Save to artifact

if __name__ == "__main__":
    main()
