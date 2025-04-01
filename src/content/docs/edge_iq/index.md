---
title: "Edge IQ Docs"
description: "Edge IQ Docs"
sidebar:
  label: "Edge IQ"
  order: 1
hero:
  tagline: "Simplified data engineering."
  image:
    alt: "Edge IQ logo"
    dark: "../../../assets/edgeIQ-logo.svg"
    light: "../../../assets/edgeIQ-logo.svg"
  actions:
    - text: "Get Started"
      link: "/start/overview/"
      icon: right-arrow
      variant: primary
    - text: "Downloads"
      link: "/start/downloads/"
      icon: external
tableOfContents: false
---

import { Card, CardGrid } from "@astrojs/starlight/components";

<CardGrid>
  <Card title="Download" icon="pencil">
    [Download](/start/downloads/) Lyftdata binaries.
  </Card>
  <Card title="Installation" icon="pencil">
    [Install](/install/overview/) Lyftdata on your infrastructure.
  </Card>
    <Card title="Configuration" icon="pencil">
    Lyftdata [configuration](/reference/configuration/) reference.
  </Card>
  <Card title="Jobs" icon="pencil">
    Learn about [Jobs](/jobs/overview/) in Lyftdata.
  </Card>

</CardGrid>