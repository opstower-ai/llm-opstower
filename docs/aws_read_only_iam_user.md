# Creating a read-only IAM user

You can create an IAM user with read-only access for use with OpsTower.ai.

1. In the IAM Console, click on ‘Users‘ on the left or under IAM Resources. Then select ‘Add User‘.
2. Give the user a name (Eg: OpsTower) and click ‘Next‘.
3. Click the ‘Attach policies directly‘ button at the top.
4. Search for 'ReadOnlyAccess' and set 'Filter by type' to 'AWS managed - job function'.
5. Select the checkbox for the 'ReadOnlyAccess' policy and click ‘Next‘.
6. Click 'Create user'.
7. In the green confirmation banner at the top, click 'View user' button.
8. Click 'Security credentials' tab.
9. Under 'Access Keys' click the 'Create access key' button.
10. Click 'Third Party Service' and the confirmation checkbox. Click the 'next' button.
11. Leave the description blank and click 'Create access key'.
12. Click the 'Download .csv file' button and save the file to your computer. Open the file and use the keys.