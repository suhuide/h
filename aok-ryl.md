[hrf](hrf.md)  
[aok](aok.md)  
[p-diff](./files/aok/p-diff.md)


## [Requirement](https://ones.cn/wiki/#/team/VocipTXV/space/7jKfDSiJ/page/YYzHTCcX)

## Code

```c
// aok02_matter_ac
$ git clone git@hoperf-matter:matter/customerproject/aok02_matter_ac.git
$ cd aok02_matter_ac
$ git submodule init
$ git submodule update
```
## Porting
### Diff
```c
//Compare with lighting project,feature in AOK project
SOFTWARE COMPONENTS
    OpenThread
        -Stack (FTD)    //need to modify
        +Stack (MTD)    
    Silicon Labs Matter v2.7.0
        Clusters
            CHIP             
                +Unit Localization Server Cluster   
            Closures             
                +Unit Localization Server Cluster
            Genera             
                +Ethernet Network Diagnostics Server Cluster
                +ICD Management Server Cluster  //need to remove
```
```c
SOFTWARE COMPONENTS  
    Silicon Labs Matter v2.7.0
        Clusters
            Network Infrastructure
                Thread Border Router Management Server Cluster
```