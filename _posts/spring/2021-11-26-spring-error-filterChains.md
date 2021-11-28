---
title: "[Spring-Security] Error - creating bean with name 'org.springframework.security.filterChains'"
date: 2021-11-26 15:00:00 -0400
categories: java spring security filterChains
---

If you have below exception when configure spring security, check out the `security-config.xml` (name could be anything depends on your setting).

```sh
org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'org.springframework.security.filterChains': Cannot resolve reference to bean 'org.springframework.security.web.DefaultSecurityFilterChain#0' while setting bean property 'sourceList' with key [0]; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'org.springframework.security.web.DefaultSecurityFilterChain#0': Cannot resolve reference to bean 'org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter#0' while setting constructor argument with key [5]; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter#0': Cannot resolve reference to bean 'org.springframework.security.authentication.ProviderManager#0' while setting bean property 'authenticationManager'; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'org.springframework.security.authentication.ProviderManager#0': Cannot resolve reference to bean 'org.springframework.security.config.authentication.AuthenticationManagerFactoryBean#0' while setting constructor argument; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'org.springframework.security.config.authentication.AuthenticationManagerFactoryBean#0': FactoryBean threw exception on object creation; nested exception is org.springframework.beans.factory.NoSuchBeanDefinitionException: No bean named 'org.springframework.security.authenticationManager' is defined: 

Did you forget to add a global <authentication-manager> 
element to your configuration (with child <authentication-provider> elements)? 
Alternatively you can use the authentication-manager-ref attribute on your 
<http> and <global-method-security> elements.
```
Solution: To solve this problem, you need to add `<authentication-manager>` as mentioned below of the exception message in th `security-config.xml`.

The `admin` `user` here is just an example.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans:beans
	xmlns="http://www.springframework.org/schema/security"
	xmlns:beans="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans
       http://www.springframework.org/schema/beans/spring-beans-4.2.xsd
       http://www.springframework.org/schema/security
       http://www.springframework.org/schema/security/spring-security-4.2.xsd">
	<http auto-config="false">
			...
	</http>
	<authentication-manager>
		<authentication-provider>
			<user-service>
				<user name="admin" password="123"
					authorities="ROLE_USER, ROLE_ADMIN" />
				<user name="guest" password="123" authorities="ROLE_USER" />
			</user-service>
		</authentication-provider>
	</authentication-manager>
</beans:beans>
```
