from langchain import LLMChain, PromptTemplate
from .chain import llm

analyze_prompt = """ Analyzing the Maven dependency tree below, with the objective of excluding dependencies already inherent in the Java Virtual Machine (JVM). Do not rely on Maven commands for exclusion details; instead, generate a concise list that highlights the top-level dependencies, excluding specific version numbers and submodule details.

{requirement}
I think this file mostly :"""
analyze_prompt_template = PromptTemplate(
    input_variables=["requirement"],
    template=analyze_prompt,
)
analyze_chain = LLMChain(llm=llm, prompt=analyze_prompt_template)
print(analyze_chain.run("""
[INFO] Scanning for projects...
[INFO] ------------------------------------------------------------------------
[INFO] Reactor Build Order:
[INFO] 
[INFO] sky-take-out                                                       [pom]
[INFO] sky-common                                                         [jar]
[INFO] sky-pojo                                                           [jar]
[INFO] sky-server                                                         [jar]
[INFO] 
[INFO] ------------------------< com.sky:sky-take-out >------------------------
[INFO] Building sky-take-out 1.0-SNAPSHOT                                 [1/4]
[INFO]   from pom.xml
[INFO] --------------------------------[ pom ]---------------------------------
[INFO] 
[INFO] --- dependency:3.3.0:tree (default-cli) @ sky-take-out ---
[INFO] com.sky:sky-take-out:pom:1.0-SNAPSHOT
[INFO] 
[INFO] -------------------------< com.sky:sky-common >-------------------------
[INFO] Building sky-common 1.0-SNAPSHOT                                   [2/4]
[INFO]   from sky-common\pom.xml
[INFO] --------------------------------[ jar ]---------------------------------
[INFO] 
[INFO] --- dependency:3.3.0:tree (default-cli) @ sky-common ---
[INFO] com.sky:sky-common:jar:1.0-SNAPSHOT
[INFO] +- org.projectlombok:lombok:jar:1.18.20:compile
[INFO] +- com.alibaba:fastjson:jar:1.2.76:compile
[INFO] +- commons-lang:commons-lang:jar:2.6:compile
[INFO] +- org.springframework.boot:spring-boot-starter-json:jar:2.7.3:compile
[INFO] |  +- org.springframework.boot:spring-boot-starter:jar:2.7.3:compile
[INFO] |  |  +- org.springframework.boot:spring-boot:jar:2.7.3:compile
[INFO] |  |  |  \- org.springframework:spring-context:jar:5.3.22:compile
[INFO] |  |  |     +- org.springframework:spring-aop:jar:5.3.22:compile
[INFO] |  |  |     \- org.springframework:spring-expression:jar:5.3.22:compile
[INFO] |  |  +- org.springframework.boot:spring-boot-autoconfigure:jar:2.7.3:compile
[INFO] |  |  +- org.springframework.boot:spring-boot-starter-logging:jar:2.7.3:compile
[INFO] |  |  |  +- ch.qos.logback:logback-classic:jar:1.2.11:compile
[INFO] |  |  |  |  \- ch.qos.logback:logback-core:jar:1.2.11:compile
[INFO] |  |  |  +- org.apache.logging.log4j:log4j-to-slf4j:jar:2.17.2:compile
[INFO] |  |  |  |  \- org.apache.logging.log4j:log4j-api:jar:2.17.2:compile
[INFO] |  |  |  \- org.slf4j:jul-to-slf4j:jar:1.7.36:compile
[INFO] |  |  +- jakarta.annotation:jakarta.annotation-api:jar:1.3.5:compile
[INFO] |  |  +- org.springframework:spring-core:jar:5.3.22:compile
[INFO] |  |  |  \- org.springframework:spring-jcl:jar:5.3.22:compile
[INFO] |  |  \- org.yaml:snakeyaml:jar:1.30:compile
[INFO] |  +- org.springframework:spring-web:jar:5.3.22:compile
[INFO] |  |  \- org.springframework:spring-beans:jar:5.3.22:compile
[INFO] |  +- com.fasterxml.jackson.core:jackson-databind:jar:2.13.3:compile
[INFO] |  |  +- com.fasterxml.jackson.core:jackson-annotations:jar:2.13.3:compile
[INFO] |  |  \- com.fasterxml.jackson.core:jackson-core:jar:2.13.3:compile
[INFO] |  +- com.fasterxml.jackson.datatype:jackson-datatype-jdk8:jar:2.13.3:compile
[INFO] |  +- com.fasterxml.jackson.datatype:jackson-datatype-jsr310:jar:2.13.3:compile
[INFO] |  \- com.fasterxml.jackson.module:jackson-module-parameter-names:jar:2.13.3:compile
[INFO] +- io.jsonwebtoken:jjwt:jar:0.9.1:compile
[INFO] +- org.springframework.boot:spring-boot-configuration-processor:jar:2.7.3:compile
[INFO] +- com.aliyun.oss:aliyun-sdk-oss:jar:3.10.2:compile
[INFO] |  +- org.apache.httpcomponents:httpclient:jar:4.5.13:compile
[INFO] |  |  +- org.apache.httpcomponents:httpcore:jar:4.4.15:compile
[INFO] |  |  \- commons-codec:commons-codec:jar:1.15:compile
[INFO] |  +- org.jdom:jdom2:jar:2.0.6.1:compile
[INFO] |  +- org.codehaus.jettison:jettison:jar:1.1:compile
[INFO] |  |  \- stax:stax-api:jar:1.0.1:compile
[INFO] |  +- com.aliyun:aliyun-java-sdk-core:jar:3.4.0:compile
[INFO] |  +- com.aliyun:aliyun-java-sdk-ram:jar:3.0.0:compile
[INFO] |  +- com.aliyun:aliyun-java-sdk-sts:jar:3.0.0:compile
[INFO] |  +- com.aliyun:aliyun-java-sdk-ecs:jar:4.2.0:compile
[INFO] |  \- com.aliyun:aliyun-java-sdk-kms:jar:2.7.0:compile
[INFO] |     \- com.google.code.gson:gson:jar:2.9.1:compile
[INFO] +- javax.xml.bind:jaxb-api:jar:2.3.1:compile
[INFO] |  \- javax.activation:javax.activation-api:jar:1.2.0:compile
[INFO] \- com.github.wechatpay-apiv3:wechatpay-apache-httpclient:jar:0.4.8:compile
[INFO]    +- org.apache.httpcomponents:httpmime:jar:4.5.13:runtime
[INFO]    \- org.slf4j:slf4j-api:jar:1.7.36:compile
[INFO] 
[INFO] --------------------------< com.sky:sky-pojo >--------------------------
[INFO] Building sky-pojo 1.0-SNAPSHOT                                     [3/4]
[INFO]   from sky-pojo\pom.xml
[INFO] --------------------------------[ jar ]---------------------------------
[INFO] 
[INFO] --- dependency:3.3.0:tree (default-cli) @ sky-pojo ---
[INFO] com.sky:sky-pojo:jar:1.0-SNAPSHOT
[INFO] +- org.projectlombok:lombok:jar:1.18.20:compile
[INFO] +- com.fasterxml.jackson.core:jackson-databind:jar:2.9.2:compile
[INFO] |  +- com.fasterxml.jackson.core:jackson-annotations:jar:2.13.3:compile
[INFO] |  \- com.fasterxml.jackson.core:jackson-core:jar:2.13.3:compile
[INFO] \- com.github.xiaoymin:knife4j-spring-boot-starter:jar:3.0.2:compile
[INFO]    +- com.github.xiaoymin:knife4j-spring-boot-autoconfigure:jar:3.0.2:compile
[INFO]    |  +- com.github.xiaoymin:knife4j-spring:jar:3.0.2:compile
[INFO]    |  |  +- com.github.xiaoymin:knife4j-annotations:jar:3.0.2:compile
[INFO]    |  |  |  +- io.swagger:swagger-annotations:jar:1.5.22:compile
[INFO]    |  |  |  \- io.swagger.core.v3:swagger-annotations:jar:2.1.2:compile
[INFO]    |  |  +- com.github.xiaoymin:knife4j-core:jar:3.0.2:compile
[INFO]    |  |  +- org.javassist:javassist:jar:3.25.0-GA:compile
[INFO]    |  |  +- io.springfox:springfox-swagger2:jar:3.0.0:compile
[INFO]    |  |  |  +- io.springfox:springfox-spi:jar:3.0.0:compile
[INFO]    |  |  |  +- io.springfox:springfox-schema:jar:3.0.0:compile
[INFO]    |  |  |  +- io.springfox:springfox-swagger-common:jar:3.0.0:compile
[INFO]    |  |  |  +- io.springfox:springfox-spring-web:jar:3.0.0:compile
[INFO]    |  |  |  |  \- io.github.classgraph:classgraph:jar:4.8.83:compile
[INFO]    |  |  |  +- io.springfox:springfox-spring-webflux:jar:3.0.0:compile
[INFO]    |  |  |  \- org.mapstruct:mapstruct:jar:1.3.1.Final:runtime
[INFO]    |  |  +- io.springfox:springfox-spring-webmvc:jar:3.0.0:compile
[INFO]    |  |  |  \- io.springfox:springfox-core:jar:3.0.0:compile
[INFO]    |  |  |     \- net.bytebuddy:byte-buddy:jar:1.12.13:compile
[INFO]    |  |  +- io.springfox:springfox-oas:jar:3.0.0:compile
[INFO]    |  |  |  \- io.swagger.core.v3:swagger-models:jar:2.1.2:compile
[INFO]    |  |  +- io.springfox:springfox-bean-validators:jar:3.0.0:compile
[INFO]    |  |  +- io.swagger:swagger-models:jar:1.5.22:compile
[INFO]    |  |  \- io.swagger:swagger-core:jar:1.5.22:compile
[INFO]    |  |     +- org.apache.commons:commons-lang3:jar:3.12.0:compile
[INFO]    |  |     +- com.fasterxml.jackson.dataformat:jackson-dataformat-yaml:jar:2.13.3:compile
[INFO]    |  |     |  \- org.yaml:snakeyaml:jar:1.30:compile
[INFO]    |  |     +- com.google.guava:guava:jar:27.0.1-android:compile
[INFO]    |  |     |  +- com.google.guava:failureaccess:jar:1.0.1:compile
[INFO]    |  |     |  +- com.google.guava:listenablefuture:jar:9999.0-empty-to-avoid-conflict-with-guava:compile
[INFO]    |  |     |  +- com.google.code.findbugs:jsr305:jar:3.0.2:compile
[INFO]    |  |     |  +- org.checkerframework:checker-compat-qual:jar:2.5.2:compile
[INFO]    |  |     |  +- com.google.errorprone:error_prone_annotations:jar:2.2.0:compile
[INFO]    |  |     |  +- com.google.j2objc:j2objc-annotations:jar:1.1:compile
[INFO]    |  |     |  \- org.codehaus.mojo:animal-sniffer-annotations:jar:1.17:compile
[INFO]    |  |     \- javax.validation:validation-api:jar:2.0.1.Final:compile
[INFO]    |  \- io.springfox:springfox-boot-starter:jar:3.0.0:compile
[INFO]    |     +- io.springfox:springfox-data-rest:jar:3.0.0:compile
[INFO]    |     +- com.fasterxml:classmate:jar:1.5.1:compile
[INFO]    |     +- org.slf4j:slf4j-api:jar:1.7.36:compile
[INFO]    |     +- org.springframework.plugin:spring-plugin-core:jar:2.0.0.RELEASE:compile
[INFO]    |     |  +- org.springframework:spring-beans:jar:5.3.22:compile
[INFO]    |     |  |  \- org.springframework:spring-core:jar:5.3.22:compile
[INFO]    |     |  |     \- org.springframework:spring-jcl:jar:5.3.22:compile
[INFO]    |     |  +- org.springframework:spring-context:jar:5.3.22:compile
[INFO]    |     |  |  \- org.springframework:spring-expression:jar:5.3.22:compile
[INFO]    |     |  \- org.springframework:spring-aop:jar:5.3.22:compile
[INFO]    |     \- org.springframework.plugin:spring-plugin-metadata:jar:2.0.0.RELEASE:compile
[INFO]    \- com.github.xiaoymin:knife4j-spring-ui:jar:3.0.2:compile
[INFO] 
[INFO] -------------------------< com.sky:sky-server >-------------------------
[INFO] Building sky-server 1.0-SNAPSHOT                                   [4/4]
[INFO]   from sky-server\pom.xml
[INFO] --------------------------------[ jar ]---------------------------------
[INFO] 
[INFO] --- dependency:3.3.0:tree (default-cli) @ sky-server ---
[INFO] com.sky:sky-server:jar:1.0-SNAPSHOT
[INFO] +- com.sky:sky-common:jar:1.0-SNAPSHOT:compile
[INFO] |  +- commons-lang:commons-lang:jar:2.6:compile
[INFO] |  +- org.springframework.boot:spring-boot-starter-json:jar:2.7.3:compile
[INFO] |  |  +- com.fasterxml.jackson.datatype:jackson-datatype-jdk8:jar:2.13.3:compile
[INFO] |  |  +- com.fasterxml.jackson.datatype:jackson-datatype-jsr310:jar:2.13.3:compile
[INFO] |  |  \- com.fasterxml.jackson.module:jackson-module-parameter-names:jar:2.13.3:compile
[INFO] |  +- io.jsonwebtoken:jjwt:jar:0.9.1:compile
[INFO] |  +- com.aliyun.oss:aliyun-sdk-oss:jar:3.10.2:compile
[INFO] |  |  +- org.apache.httpcomponents:httpclient:jar:4.5.13:compile
[INFO] |  |  |  \- org.apache.httpcomponents:httpcore:jar:4.4.15:compile
[INFO] |  |  +- org.jdom:jdom2:jar:2.0.6.1:compile
[INFO] |  |  +- org.codehaus.jettison:jettison:jar:1.1:compile
[INFO] |  |  |  \- stax:stax-api:jar:1.0.1:compile
[INFO] |  |  +- com.aliyun:aliyun-java-sdk-core:jar:3.4.0:compile
[INFO] |  |  +- com.aliyun:aliyun-java-sdk-ram:jar:3.0.0:compile
[INFO] |  |  +- com.aliyun:aliyun-java-sdk-sts:jar:3.0.0:compile
[INFO] |  |  +- com.aliyun:aliyun-java-sdk-ecs:jar:4.2.0:compile
[INFO] |  |  \- com.aliyun:aliyun-java-sdk-kms:jar:2.7.0:compile
[INFO] |  |     \- com.google.code.gson:gson:jar:2.9.1:compile
[INFO] |  \- com.github.wechatpay-apiv3:wechatpay-apache-httpclient:jar:0.4.8:compile
[INFO] |     \- org.apache.httpcomponents:httpmime:jar:4.5.13:runtime
[INFO] +- com.sky:sky-pojo:jar:1.0-SNAPSHOT:compile
[INFO] |  \- com.fasterxml.jackson.core:jackson-databind:jar:2.13.3:compile
[INFO] |     +- com.fasterxml.jackson.core:jackson-annotations:jar:2.13.3:compile
[INFO] |     \- com.fasterxml.jackson.core:jackson-core:jar:2.13.3:compile
[INFO] +- org.springframework.boot:spring-boot-starter:jar:2.7.3:compile
[INFO] |  +- org.springframework.boot:spring-boot:jar:2.7.3:compile
[INFO] |  |  \- org.springframework:spring-context:jar:5.3.22:compile
[INFO] |  +- org.springframework.boot:spring-boot-autoconfigure:jar:2.7.3:compile
[INFO] |  +- org.springframework.boot:spring-boot-starter-logging:jar:2.7.3:compile
[INFO] |  |  +- ch.qos.logback:logback-classic:jar:1.2.11:compile
[INFO] |  |  |  \- ch.qos.logback:logback-core:jar:1.2.11:compile
[INFO] |  |  +- org.apache.logging.log4j:log4j-to-slf4j:jar:2.17.2:compile
[INFO] |  |  |  \- org.apache.logging.log4j:log4j-api:jar:2.17.2:compile
[INFO] |  |  \- org.slf4j:jul-to-slf4j:jar:1.7.36:compile
[INFO] |  +- jakarta.annotation:jakarta.annotation-api:jar:1.3.5:compile
[INFO] |  +- org.springframework:spring-core:jar:5.3.22:compile
[INFO] |  |  \- org.springframework:spring-jcl:jar:5.3.22:compile
[INFO] |  \- org.yaml:snakeyaml:jar:1.30:compile
[INFO] +- org.springframework.boot:spring-boot-starter-test:jar:2.7.3:test
[INFO] |  +- org.springframework.boot:spring-boot-test:jar:2.7.3:test
[INFO] |  +- org.springframework.boot:spring-boot-test-autoconfigure:jar:2.7.3:test
[INFO] |  +- com.jayway.jsonpath:json-path:jar:2.7.0:test
[INFO] |  |  \- net.minidev:json-smart:jar:2.4.8:test
[INFO] |  |     \- net.minidev:accessors-smart:jar:2.4.8:test
[INFO] |  |        \- org.ow2.asm:asm:jar:9.1:test
[INFO] |  +- jakarta.xml.bind:jakarta.xml.bind-api:jar:2.3.3:test
[INFO] |  |  \- jakarta.activation:jakarta.activation-api:jar:1.2.2:test
[INFO] |  +- org.assertj:assertj-core:jar:3.22.0:test
[INFO] |  +- org.hamcrest:hamcrest:jar:2.2:test
[INFO] |  +- org.junit.jupiter:junit-jupiter:jar:5.8.2:test
[INFO] |  |  +- org.junit.jupiter:junit-jupiter-api:jar:5.8.2:test
[INFO] |  |  |  +- org.opentest4j:opentest4j:jar:1.2.0:test
[INFO] |  |  |  +- org.junit.platform:junit-platform-commons:jar:1.8.2:test
[INFO] |  |  |  \- org.apiguardian:apiguardian-api:jar:1.1.2:test
[INFO] |  |  +- org.junit.jupiter:junit-jupiter-params:jar:5.8.2:test
[INFO] |  |  \- org.junit.jupiter:junit-jupiter-engine:jar:5.8.2:test
[INFO] |  |     \- org.junit.platform:junit-platform-engine:jar:1.8.2:test
[INFO] |  +- org.mockito:mockito-core:jar:4.5.1:test
[INFO] |  |  +- net.bytebuddy:byte-buddy:jar:1.12.13:compile
[INFO] |  |  +- net.bytebuddy:byte-buddy-agent:jar:1.12.13:test
[INFO] |  |  \- org.objenesis:objenesis:jar:3.2:test
[INFO] |  +- org.mockito:mockito-junit-jupiter:jar:4.5.1:test
[INFO] |  +- org.skyscreamer:jsonassert:jar:1.5.1:test
[INFO] |  |  \- com.vaadin.external.google:android-json:jar:0.0.20131108.vaadin1:test
[INFO] |  +- org.springframework:spring-test:jar:5.3.22:test
[INFO] |  \- org.xmlunit:xmlunit-core:jar:2.9.0:test
[INFO] +- org.springframework.boot:spring-boot-starter-web:jar:2.7.3:compile
[INFO] |  +- org.springframework.boot:spring-boot-starter-tomcat:jar:2.7.3:compile
[INFO] |  |  +- org.apache.tomcat.embed:tomcat-embed-core:jar:9.0.65:compile
[INFO] |  |  +- org.apache.tomcat.embed:tomcat-embed-el:jar:9.0.65:compile
[INFO] |  |  \- org.apache.tomcat.embed:tomcat-embed-websocket:jar:9.0.65:compile
[INFO] |  +- org.springframework:spring-web:jar:5.3.22:compile
[INFO] |  |  \- org.springframework:spring-beans:jar:5.3.22:compile
[INFO] |  \- org.springframework:spring-webmvc:jar:5.3.22:compile
[INFO] |     +- org.springframework:spring-aop:jar:5.3.22:compile
[INFO] |     \- org.springframework:spring-expression:jar:5.3.22:compile
[INFO] +- mysql:mysql-connector-java:jar:8.0.30:runtime
[INFO] +- org.mybatis.spring.boot:mybatis-spring-boot-starter:jar:2.2.0:compile
[INFO] |  +- org.springframework.boot:spring-boot-starter-jdbc:jar:2.7.3:compile
[INFO] |  |  +- com.zaxxer:HikariCP:jar:4.0.3:compile
[INFO] |  |  \- org.springframework:spring-jdbc:jar:5.3.22:compile
[INFO] |  +- org.mybatis.spring.boot:mybatis-spring-boot-autoconfigure:jar:2.2.0:compile
[INFO] |  +- org.mybatis:mybatis:jar:3.5.7:compile
[INFO] |  \- org.mybatis:mybatis-spring:jar:2.0.6:compile
[INFO] +- org.projectlombok:lombok:jar:1.18.20:compile
[INFO] +- com.alibaba:fastjson:jar:1.2.76:compile
[INFO] +- com.alibaba:druid-spring-boot-starter:jar:1.2.1:compile
[INFO] |  +- com.alibaba:druid:jar:1.2.1:compile
[INFO] |  |  \- javax.annotation:javax.annotation-api:jar:1.3.2:compile
[INFO] |  \- org.slf4j:slf4j-api:jar:1.7.36:compile
[INFO] +- com.github.pagehelper:pagehelper-spring-boot-starter:jar:1.3.0:compile
[INFO] |  +- com.github.pagehelper:pagehelper-spring-boot-autoconfigure:jar:1.3.0:compile
[INFO] |  \- com.github.pagehelper:pagehelper:jar:5.2.0:compile
[INFO] |     \- com.github.jsqlparser:jsqlparser:jar:3.2:compile
[INFO] +- org.aspectj:aspectjrt:jar:1.9.4:compile
[INFO] +- org.aspectj:aspectjweaver:jar:1.9.4:compile
[INFO] +- com.github.xiaoymin:knife4j-spring-boot-starter:jar:3.0.2:compile
[INFO] |  +- com.github.xiaoymin:knife4j-spring-boot-autoconfigure:jar:3.0.2:compile
[INFO] |  |  +- com.github.xiaoymin:knife4j-spring:jar:3.0.2:compile
[INFO] |  |  |  +- com.github.xiaoymin:knife4j-annotations:jar:3.0.2:compile
[INFO] |  |  |  |  +- io.swagger:swagger-annotations:jar:1.5.22:compile
[INFO] |  |  |  |  \- io.swagger.core.v3:swagger-annotations:jar:2.1.2:compile
[INFO] |  |  |  +- com.github.xiaoymin:knife4j-core:jar:3.0.2:compile
[INFO] |  |  |  +- org.javassist:javassist:jar:3.25.0-GA:compile
[INFO] |  |  |  +- io.springfox:springfox-swagger2:jar:3.0.0:compile
[INFO] |  |  |  |  +- io.springfox:springfox-spi:jar:3.0.0:compile
[INFO] |  |  |  |  +- io.springfox:springfox-schema:jar:3.0.0:compile
[INFO] |  |  |  |  +- io.springfox:springfox-swagger-common:jar:3.0.0:compile
[INFO] |  |  |  |  +- io.springfox:springfox-spring-web:jar:3.0.0:compile
[INFO] |  |  |  |  |  \- io.github.classgraph:classgraph:jar:4.8.83:compile
[INFO] |  |  |  |  +- io.springfox:springfox-spring-webflux:jar:3.0.0:compile
[INFO] |  |  |  |  \- org.mapstruct:mapstruct:jar:1.3.1.Final:runtime
[INFO] |  |  |  +- io.springfox:springfox-spring-webmvc:jar:3.0.0:compile
[INFO] |  |  |  |  \- io.springfox:springfox-core:jar:3.0.0:compile
[INFO] |  |  |  +- io.springfox:springfox-oas:jar:3.0.0:compile
[INFO] |  |  |  |  \- io.swagger.core.v3:swagger-models:jar:2.1.2:compile
[INFO] |  |  |  +- io.springfox:springfox-bean-validators:jar:3.0.0:compile
[INFO] |  |  |  +- io.swagger:swagger-models:jar:1.5.22:compile
[INFO] |  |  |  \- io.swagger:swagger-core:jar:1.5.22:compile
[INFO] |  |  |     +- org.apache.commons:commons-lang3:jar:3.12.0:compile
[INFO] |  |  |     +- com.fasterxml.jackson.dataformat:jackson-dataformat-yaml:jar:2.13.3:compile
[INFO] |  |  |     +- com.google.guava:guava:jar:27.0.1-android:compile
[INFO] |  |  |     |  +- com.google.guava:failureaccess:jar:1.0.1:compile
[INFO] |  |  |     |  +- com.google.guava:listenablefuture:jar:9999.0-empty-to-avoid-conflict-with-guava:compile
[INFO] |  |  |     |  +- com.google.code.findbugs:jsr305:jar:3.0.2:compile
[INFO] |  |  |     |  +- org.checkerframework:checker-compat-qual:jar:2.5.2:compile
[INFO] |  |  |     |  +- com.google.errorprone:error_prone_annotations:jar:2.2.0:compile
[INFO] |  |  |     |  +- com.google.j2objc:j2objc-annotations:jar:1.1:compile
[INFO] |  |  |     |  \- org.codehaus.mojo:animal-sniffer-annotations:jar:1.17:compile
[INFO] |  |  |     \- javax.validation:validation-api:jar:2.0.1.Final:compile
[INFO] |  |  \- io.springfox:springfox-boot-starter:jar:3.0.0:compile
[INFO] |  |     +- io.springfox:springfox-data-rest:jar:3.0.0:compile
[INFO] |  |     +- com.fasterxml:classmate:jar:1.5.1:compile
[INFO] |  |     +- org.springframework.plugin:spring-plugin-core:jar:2.0.0.RELEASE:compile
[INFO] |  |     \- org.springframework.plugin:spring-plugin-metadata:jar:2.0.0.RELEASE:compile
[INFO] |  \- com.github.xiaoymin:knife4j-spring-ui:jar:3.0.2:compile
[INFO] +- org.springframework.boot:spring-boot-starter-data-redis:jar:2.7.3:compile
[INFO] |  +- org.springframework.data:spring-data-redis:jar:2.7.2:compile
[INFO] |  |  +- org.springframework.data:spring-data-keyvalue:jar:2.7.2:compile
[INFO] |  |  |  \- org.springframework.data:spring-data-commons:jar:2.7.2:compile
[INFO] |  |  +- org.springframework:spring-tx:jar:5.3.22:compile
[INFO] |  |  \- org.springframework:spring-oxm:jar:5.3.22:compile
[INFO] |  \- io.lettuce:lettuce-core:jar:6.1.9.RELEASE:compile
[INFO] |     +- io.netty:netty-common:jar:4.1.79.Final:compile
[INFO] |     +- io.netty:netty-handler:jar:4.1.79.Final:compile
[INFO] |     |  +- io.netty:netty-resolver:jar:4.1.79.Final:compile
[INFO] |     |  +- io.netty:netty-buffer:jar:4.1.79.Final:compile
[INFO] |     |  +- io.netty:netty-transport-native-unix-common:jar:4.1.79.Final:compile
[INFO] |     |  \- io.netty:netty-codec:jar:4.1.79.Final:compile
[INFO] |     +- io.netty:netty-transport:jar:4.1.79.Final:compile
[INFO] |     \- io.projectreactor:reactor-core:jar:3.4.22:compile
[INFO] |        \- org.reactivestreams:reactive-streams:jar:1.0.4:compile
[INFO] +- org.springframework.boot:spring-boot-starter-cache:jar:2.7.3:compile
[INFO] |  \- org.springframework:spring-context-support:jar:5.3.22:compile
[INFO] +- org.springframework.boot:spring-boot-starter-websocket:jar:2.7.3:compile
[INFO] |  +- org.springframework:spring-messaging:jar:5.3.22:compile
[INFO] |  \- org.springframework:spring-websocket:jar:5.3.22:compile
[INFO] +- javax.xml.bind:jaxb-api:jar:2.3.1:compile
[INFO] |  \- javax.activation:javax.activation-api:jar:1.2.0:compile
[INFO] +- org.apache.poi:poi:jar:3.16:compile
[INFO] |  +- commons-codec:commons-codec:jar:1.15:compile
[INFO] |  \- org.apache.commons:commons-collections4:jar:4.1:compile
[INFO] \- org.apache.poi:poi-ooxml:jar:3.16:compile
[INFO]    +- org.apache.poi:poi-ooxml-schemas:jar:3.16:compile
[INFO]    |  \- org.apache.xmlbeans:xmlbeans:jar:2.6.0:compile
[INFO]    \- com.github.virtuald:curvesapi:jar:1.04:compile
[INFO] ------------------------------------------------------------------------
[INFO] Reactor Summary for sky-take-out 1.0-SNAPSHOT:
[INFO] 
[INFO] sky-take-out ....................................... SUCCESS [  1.026 s]
[INFO] sky-common ......................................... SUCCESS [  0.107 s]
[INFO] sky-pojo ........................................... SUCCESS [  0.087 s]
[INFO] sky-server ......................................... SUCCESS [  0.198 s]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  1.819 s
[INFO] Finished at: 2023-11-30T11:02:21+08:00
[INFO] ------------------------------------------------------------------------
"""))