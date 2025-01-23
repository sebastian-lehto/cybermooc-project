# cybermooc-project

https://github.com/sebastian-lehto/cybermooc-project
The project was made using Python and Django, and can be run the same way as the projects in the course assignments.

FLAW 1: Broken Access Control
https://github.com/sebastian-lehto/cybermooc-project/blob/main/src/profiles/views.py#L51

This flaw is an example of broken access control, as it violates the principle of least privilege and deny by default. Any user should not be able to delete another user. Only administrators should have the right to manipulate or delete other users data, and the backend should ensure that this action can only be performed by an admin account.

The fix for this flaw would deny access to this action for all users by default and only allow a user to be deleted by an admin account. This would ensure proper access control for this particular action. There are several ways to do this, including django's staff_member_required decorator or by checking the user's username. The use of the staff_member_required decorator would require large changes in implementation, but for the purposes of this application the same effect could be achieved by checking if the username of the current user is "admin" before the action is completed.

FLAW 2: Insecure design
https://github.com/sebastian-lehto/cybermooc-project/blob/main/src/profiles/urls.py#L7

This flaw is an example of insecure design. Using the users ID in urls allows users to perform actions they should not be able to. By viewing another users profile users can see the ID that is used for deleting accounts. This means that even if the previous flaw is fixed, a user can still delete another users profile. Bypassing access control checks also falls in the broken access control -category. However, the flaw is still meets the requirements of insecure design. If this application would be developed further new issues would arise as a consequence of this design-level flaw. This does not make the flaw hypothetical, as the flaw is not in any specific implementation, but rather the way the application was designed. Therefore the flaw already exists even if does not have many consequences at this stage of development.

This flaw can be fixed only by designing the software in such a way that urls do not give users critical information such as user IDs. Separating the information that is visible the the users from information used in critical backend processes should happen in the design phase. One fix for this flaw would be to use Djangos built-in permission system to make sure, that a user can only perform actions they supposed to be able to. The use of permissions would require redesigning of the project to assign permissions for different users.

FLAW 3: Sensitive data exposure
https://github.com/sebastian-lehto/cybermooc-project/blob/main/src/profiles/views.py#L37

This flaw is an example of sensitive data exposure. More specifically it is an unnecessary feature. There is no need for a separate page listing all user information. Even if it was only accessible to admin users, it would be an unnecessary feature that should be removed. This is an extreme example of sensitive data exposure as it leaves all of the users important information visible.

The fix for this flaw would be to simply remove this site altogether. If developers or administrators need to access user information, it should be done in a separate system. This kind of critical information should not be present in the frontend of the application, let alone open for all users to see.

FLAW 4: Identification and Authentication Failures
https://github.com/sebastian-lehto/cybermooc-project/blob/main/src/profiles/views.py#L27

This flaw is an example of an identification and authentication failure. Using "admin" as the username and password of an admin account is a clear failure to properly identify and authenticate users that should have access to this account. Even the most simple credential stuffing attack would make easy work of this application and allow the attacker to access all the functions that are meant only for admin users, which in this particular application are already open to all users due to flaw #1.

The fix for this flaw would be to use a stronger username-password combination for admin users. It is also recommended that important passwords should be rotated, that is to say limiting the lifetime of a password and forcing the user to change it. Another feature that would make this authentication process safer would be complexity requirements for passwords. This would mean only allowing password that are sufficiently complex to be used for authentication.

FLAW 5: Missing CSRF
https://github.com/sebastian-lehto/cybermooc-project/blob/main/src/profiles/views.py#L22

The flaw here is a missing csrf-validation. The csrf-token is missing in the HTML and the validation is also bypassed in the backend. This leaves the system open to cross-site request forgery, a form of attack that allows the use of other sites to make requests to the target application.

The fix for this flaw would be to remove the line bypassing the csrf-validation and including the token in the login form. The csrf-token would make it impossible for attackers from other sites to perform requests on the application. Removing the line bypassing the csrf-validation would make it impossible to use the login function without a token.


You can sign in to test the application with these credentials:

Username: Bob
 
Password: 1234

