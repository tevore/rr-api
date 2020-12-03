package com.tevore.rrapi.domain;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import org.springframework.data.neo4j.core.schema.*;

@Node("Wrestler")
@Getter
@Setter
@ToString
public class Wrestler {

    @Id
    private Long id;

    @Property("name")
    private String name;

    @Relationship(type = "WON")
    private Boolean won;

    public Wrestler(String name) {
        this.name = name;
    }
}
