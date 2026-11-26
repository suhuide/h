[hrf](hrf.md)  

# [SideChannel](./files/ble/sidechannel.md)  
# [MatterDFUoverBLE](./files/ble/matter-ota.md)  
# [DTM](./files/ble/dtm.md)  

<div style="display: flex; gap: 10px;">
<table style="border-collapse: collapse; width: 100%; text-align: center; font-family: sans-serif; font-size: 14px;">
  <thead>
    <tr style="background-color: #d9d9d9;">
      <th style="border: 1px solid #000; padding: 5px;">Preamble</th>
      <th style="border: 1px solid #000; padding: 5px;">Access Address</th>
      <th colspan="6" style="border: 1px solid #000; padding: 5px;">PDU (2-257 bytes)</th>
      <th style="border: 1px solid #000; padding: 5px;">CRC</th>
    </tr>
  </thead>
  <tbody>
    <!-- 第1行：基础结构 -->
    <tr>
      <td rowspan="5" style="border: 1px solid #000; padding: 5px;">
        1 byte<br>(1M PHY)<br><br>2 bytes<br>(2M PHY)
      </td>
      <td rowspan="5" style="border: 1px solid #000; padding: 5px;">
        4 bytes
      </td>
      <td style="border: 1px solid #000; padding: 5px; background-color: #e4dfdf; font-weight: bold;">LL Header</td>
      <td colspan="4" style="border: 1px solid #000; padding: 5px; background-color: #e4dfdf; font-weight: bold;">Payload (0-251 bytes)</td>
      <td rowspan="2" style="border: 1px solid #000; padding: 5px; font-weight: bold;">
        MIC<br>(Optional)
      </td>
      <td rowspan="5" style="border: 1px solid #000; padding: 5px;">
        3 bytes
      </td>
    </tr>
    <!-- 第2行：LL Header 尺寸 + L2CAP 标题 -->
    <tr>
      <td rowspan="4" style="border: 1px solid #000; padding: 5px;">2 bytes</td>
      <td style="border: 1px solid #000; padding: 5px; font-weight: bold;">L2CAP<br>Header</td>
      <!-- ATT Data 仅占这一行的高度 -->
      <td colspan="4" style="border: 1px solid #000; padding: 5px; font-weight: bold;">ATT Data (0-247 bytes)</td>
    </tr>
    <!-- 第3行：L2CAP 的尺寸(跨两行) + ATT Header 和 Payload 分割 -->
    <tr>
      <!-- 关键修复点 1：让 4 bytes 跨 2 行，这样它的底边才能和下面 1 byte/2 bytes 齐平 -->
      <td rowspan="3" style="border: 1px solid #000; padding: 5px; vertical-align: middle; font-weight: bold;">4 bytes</td>
      <td colspan="2" style="border: 1px solid #000; padding: 5px; background-color: #f0f0f0; font-weight: bold;">ATT Header</td>
      <!-- 关键修复点 2：ATT Payload 仅跨 2 行 -->
      <td rowspan="1" style="border: 1px solid #000; padding: 5px; vertical-align: middle; background-color: #f0f0f0; font-weight: bold;">ATT Payload</td>
      <td rowspan="3" style="border: 1px solid #000; padding: 5px; vertical-align: middle;">4 bytes</td>
    </tr>
    <!-- 第4行：ATT Header 内部细分 -->
    <tr>
      <td style="border: 1px solid #000; padding: 5px; font-weight: bold;">Op Code</td>
      <td style="border: 1px solid #000; padding: 5px; font-weight: bold;">Attribute Handle</td>
      <td rowspan="2" style="border: 1px solid #000; padding: 5px;">Up to 244 bytes</td>
    </tr>
    <!-- 第5行：底层数据大小 (这里不再需要横向跨越) -->
    <tr>
      <!-- 注意：因为 4 bytes 已经在上一行占用了左侧的位置，这里直接接后面的列 -->
      <td style="border: 1px solid #000; padding: 5px;">1 byte</td>
      <td style="border: 1px solid #000; padding: 5px;">2 bytes</td>
    </tr>
  </tbody>
</table>
</div>