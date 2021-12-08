---
title: "[Java] Custom HTTP RequestURL XSS Filter"
date: 2021-12-09 15:00:00 -0400
categories: java http request XSS filter prevent cross scripting attack
---

Sample to show how to check requestURL and prevent Croos-Site-Script Attack
Using common XSS Filter to convert URL to clean string.

```java
package com.handler.filter;

import java.io.IOException;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.http.HttpServletRequest;

public class XSSFilter implements Filter {
	@Override
	public void init(FilterConfig filterConfig) throws ServletException {
	}

	@Override
	public void destroy() {
	}

	@Override
	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
		String requestURI = ((HttpServletRequest) request).getRequestURI();
		String newURI = cleanXSS(requestURI);
		request.getRequestDispatcher(newURI).forward(request, response);
		chain.doFilter(request, response);
	}

	private String cleanXSS(String value) {
		value = value.replaceAll("<", "& lt;").replaceAll(">", "& gt;");
		value = value.replaceAll("\\(", "& #40;").replaceAll("\\)", "& #41;");
		value = value.replaceAll("'", "& #39;");
		value = value.replaceAll("eval\\((.*)\\)", "");
		value = value.replaceAll("[\\\"\\\'][\\s]*javascript:(.*)[\\\"\\\']", "\"\"");
		value = value.replaceAll("script", "");
		return value;
	}

}
```

Then set filter in the `web.xml`

```xml
<filter>
    <filter-name>XSSFilter</filter-name>
    <filter-class>com.handler.filter.XSSFilter</filter-class>
</filter>
<filter-mapping>
    <filter-name>XSSFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```
