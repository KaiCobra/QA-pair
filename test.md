# 一次看飽飽所有langgraph範例
> 實用而且對於波特人 roadmap 重要的

## 各種客服問答轉發讓不同代理人回答 ([customer-support.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/chatbots/customer-support.ipynb))

**音樂代理人（Music Agent）** ：搜索特定歌手的歌曲或專輯。

**帳號代理人（Account Agent）** ：更新個人資料或查詢帳戶訂單狀態。

**通用代理人（Generic Agent）** ：根據用戶的初始查詢來判斷應該將用戶導向哪個專門代理人，從而提供更專業化的服務。

* **流暢的顧客服務體驗** ：通過使用專門的代理人處理具體的查詢範疇，能夠更有效率地滿足用戶需求，同時減少錯誤和誤解。
* **有效資源分配** ：通過將請求分派給最合適的代理人，確保每個查詢都由最適合處理該問題的代理人來回答，從而提高了整體服務的質量。
* **自動化查詢處理** ：機器人可以自動識別和轉發用戶問題到相關部門，降低人工介入的需要，增強處理速度和準確性。

## 動態收集使用者需求、自動解題 ([information-gather-prompting.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/chatbots/information-gather-prompting.ipynb))

**收集需求階段** ：聊天機器人先詢問用戶關於他們想要創建的提示模板的具體需求，如模板的目標、將傳入模板的變數、輸出的限制條件和必須遵循的規則。

**根據需求生成提示** ：一旦所有資訊被收集並透過特定工具調用，機器人便根據用戶所提供的資料生成一個定制的提示模板。

**模板細化** ：生成的提示模板可以根據用戶的進一步反饋進行調整和細化。

## 多代理英國五年GDP折線圖 ([multi-agent-collaboration.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/multi_agent/multi-agent-collaboration.ipynb))

**解決的情境問題** ： 在這個情境中，我們的目標是獲取英國過去5年的GDP數據並繪製成折線圖。這涉及到兩個主要任務：一個代理專門用於研究相關數據，另一個代理專門用於生成折線圖。通過這種方式，我們可以利用不同代理的專業知識和工具，以最有效的方式完成任務。

## 多代理一團上網研究一團寫 ([hierarchical_agent_teams.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/multi_agent/hierarchical_agent_teams.ipynb))

情境一：研究團隊

* **任務** ：查找有關「Taylor Swift 的下一次巡演」的資訊。
* **解決方案** ：研究團隊首先使用搜索代理人查詢，然後使用網頁抓取代理人從特定網址提取。這一過程由一個小組監督者協調，決定何時完成搜索工作並將任務轉交給下一個代理人或宣布任務完成。

情境二：文件撰寫團隊

* **任務** ：撰寫一首詩的大綱，然後將詩歌保存到磁盤上。
* 解決方案：文件撰寫團隊包含多個專門的代理人，包括筆記代理人負責撰寫大綱，文件編輯代理人進行文件保存和編輯，以及圖表生成代理人專注於數據視覺化。這個流程同樣由一個小組監督者來協調和決定任務的轉交和完成。

## 多代理上網做研究、寫程式碼 ([agent_supervisor.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/multi_agent/agent_supervisor.ipynb))

第一個例子：編寫並執行程式代碼

* **用戶請求** ：「編寫Hello World程式並在終端機上顯示它」
* **情境解決** ：在此情境下，代理人監督者接收到用戶請求後，分析請求的性質，並將任務分派給「程式編寫者」節點。程式編寫者節點則具體執行編寫和運行程式代碼的工作，並將結果回報。這個過程自動化了軟件開發中常見的編碼任務，提高了處理速度並減少了人為錯誤。

第二個例子：撰寫關於高山鼠兔的研究報告

* **用戶請求** ：「撰寫一份關於高山鼠兔的簡短研究報告」
* **情境解決** ：在這個例子中，代理人監督者判斷這是一個需要資訊搜集和文獻研究的任務，因此將請求轉交給「研究者」節點。研究者節點通過網路搜索和資料整理，生成了一份詳細的研究報告，有效地解答了用戶的問題。這不僅提高了資訊收集的效率，也確保了報告的質量和準確性。

## 自動生成維基百科 ([storm.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/storm/storm.ipynb))

STORM 是一個研究助手，基於大綱的 RAG 概念，生成維基百科風格文章。
傳統的文章生成方法可能會受限於片段組合，而 STORM 則採用了更加結構化的方法，通過生成大綱、模擬多角度對話等方式，確保生成的文章更具組織性和全面性。

1. 生成初始大綱： 根據用戶提供的主題，使用快速的語言模型生成初始的大綱，作為後續研究的基礎。
2. 擴展相關主題： 利用搜索引擎生成相關主題列表，擴展研究範圍，從不同角度深入了解主題。
3. 生成多個觀點： 選擇代表性的維基百科編輯，模擬他們的角度進行對話，從而確保文章的多角度覆蓋。
4. 專家訪談： 模擬與專家的對話，從專家回答中提取引用的參考文獻，並保存到向量存儲中。
5. 精煉大綱和撰寫文章： 根據專家訪談的結果和引用的參考文獻，進一步精煉大綱，最終撰寫完整的文章。

## 自適應RAG ([langgraph_adaptive_rag.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/rag/langgraph_adaptive_rag.ipynb))

Adaptive RAG 的開發動機在於提供一種更靈活的 RAG 策略，以滿足用戶對於不同類型問題的查詢需求。傳統的 RAG 模型可能會在處理不同類型問題時存在固定的策略，而 Adaptive RAG 則可以根據問題的性質進行靈活調整，從而提高搜索效率和準確性。

Adaptive RAG 的使用可以帶來多方面的效益：

1. **智慧路由：** Adaptive RAG 可以根據問題選擇不同的數據源進行搜索。
2. **主動校正：** Adaptive RAG 主動校正的功能，根據搜索結果自我調整。
3. **多源搜索：** Adaptive RAG 可以結合網路搜索和向量存儲。

## 自動寫程式、自定義評估 ([langgraph_code_assistant.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/code_assistant/langgraph_code_assistant.ipynb))

1. **讀檔和 LLM 選擇：** 我們從用戶指定的 LCEL（LangChain 表達語言）檔，並使用長上下文的 LLM 進行程式生成。
2. 程式**生成鏈：** 我們構建了程式生成鏈，其中包括使用 OpenAI 和 Claude3 的功能調用。該鏈可以根據檔案和用戶問題生成程式解決方案。
3. **控制流圖：** 我們使用 LangGraph 構建了一個控制流圖，定義了生成程式、檢查程式和反思的邏輯流程。這有助於自動化程式生成過程並進行單元測試。
4. **自定義評估：** 我們定義了自定義的評估函數，用於比較使用 LangGraph 和基礎情境塞入（Context Stuffing）方法生成的程式性能。這有助於評估 LangGraph 的效果。

> 可套用政府領域應用

## 視覺化圖表graphviz、Mermaid轉png ([visualization.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/visualization.ipynb))

Ascii視覺化、Mermaid視覺化、PNG圖片

## 規劃後執行 ([plan-and-execute.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/plan-and-execute/plan-and-execute.ipynb))

建立一個”規劃和執行”風格的代理人，這受到了”規劃和解決”論文以及 Baby-AGI 項目的啟發。其核心思想是首先制定一個多步規劃，然後逐步執行該規劃中的每一項任務。在完成特定任務後，您可以重新檢視規劃並進行必要的修改。

這種”規劃和執行”風格的代理人與 typcal 的 ReAct 相比有以下優點：

1. **明確的長期計畫：** 即使是非常強大的 LLM，也可能很難進行長期規劃。這種風格的代理人能夠明確地制定長期規劃。
2. **能夠使用較小/較弱的模型進行執行步驟：** 我們可以將較大/較好的模型僅用於規劃步驟，而將較小/較弱的模型用於執行步驟。

## 超越「思維樹」的「語言樹」 ([lats.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/lats/lats.ipynb))

語言代理樹搜索（Language Agent Tree Search，簡稱 LATS）由 Zhou 等人提出，是一個結合反思/評估和搜索（特別是蒙特卡羅樹搜索）的一般性語言模型代理搜索算法。這種方法比類似的技術如 ReACT、Reflexion 或 Tree of Thoughts 表現出更好的整體任務效能。

具體例子及解決的情境問題：

**搜尋過程** ：

* **選擇** ：基於之前步驟累積的獎勵選擇最佳的下一步動作。如果找到解決方案或達到最大搜索深度則回應，否則繼續搜索。
* **擴展和模擬** ：選擇「最佳的」5個潛在動作並並行執行它們。
* **反思 + 評估** ：觀察這些動作的結果並基於反思（可能還包括外部反饋）對決策進行評分。
* **反向傳播** ：根據結果更新根軌跡的得分。

**例子的運用** ：

* **查詢解決方案** ：例如，生成與特定主題相關的表格或策略建議。這個例子中，代理樹搜索被用來生成關於特定鳥類的平均尺寸和重量，以及最古老的記錄實例的表格。
* **策略建議** ：另一個例子是對棋局的分析，如 Magnus Carlsen 對 Alireza Firouzja 的棋局分析並提出替代策略。

**解決的情境問題** ：

* **復雜任務的高效處理** ：LATS 通過樹狀結構的搜索使得處理復雜的問題查詢更為高效，能夠探索多個可能的解決方案。
* **動態決策制定** ：反思和評估機制使代理能夠在搜索過程中動態地調整策略，以尋找更優的解決方案。
* **提升解決方案的**品質：通過在每一步反向傳播更新解決方案的評分，代理能夠根據過往的表現和反饋不斷改進其行動決策。

## 複雜任務可安排先後次序、最小化成本 ([LLMCompiler.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/llm-compiler/LLMCompiler.ipynb))

LLMCompiler 這個系統是設計來優化和加速執行代理任務的過程，尤其是在需要處理多個異步任務時。此系統通過有計劃地分配和執行這些任務，大大減少了對語言模型的呼叫次數，從而節約了成本並提高了效率。

假設有一個問題：「紐約州的GDP是多少？」這個問題需要系統執行多步驟的數據檢索和處理才能解答。這些步驟可能包括檢索有關紐約州經濟的文章、計算與GDP相關的數據等。

**計劃階段（Planner）** ：

* 首先，LLMCompiler 的「Planner」組件會生成一個計劃，這個計劃會標明執行每一步任務的順序和依賴關係。例如，首先搜索紐約州的經濟資料，然後計算或提取GDP相關數據。

**任務提取單元（Task Fetching Unit）**

* 一旦「Planner」生成計劃，「Task Fetching Unit」就會根據計劃開始執行這些任務。這一過程中，只有當一個任務的所有前置任務完成後，它才會開始執行，確保了執行的有效性和正確性。

**合併組件（Joiner）** ：

* 當所有的任務執行完畢後，「Joiner」將根據這些任務的輸出來組織和生成最終的用戶回應。如果計劃需要重新評估或更多的數據檢索，「Joiner」可能會觸發第二輪計劃的生成和執行。

這個過程不僅提高了任務處理的速度，還通過減少對語言模型的不必要調用來降低成本。在大規模或復雜的查詢中，這種方法能有效提升系統的整體性能和可擴展性。

## [一次先規劃好，才分頭去執行，最小化成本 (](https://github.com/langchain-ai/langgraph/blob/main/examples/rewoo/rewoo.ipynb)[rewoo.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/rewoo/rewoo.ipynb)[)](https://github.com/langchain-ai/langgraph/blob/main/examples/rewoo/rewoo.ipynb)

在ReWOO架構下，具體的應用實例如下：

假設你需要解答一個問題：「2024年澳洲網球公開賽冠軍的家鄉是哪裡？」這個問題需要多步驟的資訊檢索和處理。

**規劃（Planner）** ：

* **規劃** ：Planner使用一次LLM調用生成整個任務計劃，這大大節省了在每一步重複調用LLM的需要，也減少了因重複提供前置步驟內容而增加的token消耗。
* **輸出** ：例如，Planner首先計劃使用Google工具查找「2024年澳洲網球公開賽冠軍是誰」，然後使用這些信息來尋找冠軍的家鄉。

**執行者（Worker）** ：

* **執行** ：根據Planner生成的計劃，Worker按順序執行計劃中指定的工具調用。例如，首先調用搜索引擎查找賽事冠軍，再查找其家鄉。
* **效率** ：由於計劃已經明確，不需要中途等待或重新生成計劃，所以整個過程的執行時間被最小化。

**求解器（Solver）** ：

* **生成答案** ：Solver根據Worker提供的所有工具調用的結果來生成最終答案。例如，根據搜索到的冠軍姓名，進一步確認他的家鄉，並給出最終的回答。
* **直接回應** ：Solver直接利用前面步驟的結果來回答原始問題，避免了在回答生成過程中進行不必要的數據處理或再次調用LLM。

優點總結

* **效率** ：通過在計劃階段就預先確定好所有步驟，ReWOO極大地減少了運行時的延遲和資源消耗。
* **精簡** ：因為不需要在每一步都提供完整的前置步驟內容，所以減少了重複的token使用，這對於處理大規模數據或在token限制嚴格的環境中尤其有利。
* **可擴展性** ：這種架構可以輕易地擴展到更複雜的問題解決場景，並且能夠有效利用多種工具和資源。

> 基礎結構

## **非同步 (** [async.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/async.ipynb))

在這個例子中，我們將建立一個聊天執行器，其中包含核心邏輯的本機非同步實現。這使得可以利用具有非同步客戶端的聊天模型，無需在單獨的線程中調用模型。

## **支持者與反對者的辯論 (** [branching.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/branching.ipynb))

對者角色能讓對話更多元，增添趣味，並幫助用戶更深入思考問題，提高辯論能力。定義了兩個分支，一個是支持者(proponent)，一個是反對者(opponent)。支持者會以積極的態度回答用戶的問題，而反對者則會以批評的角度回答。接著，定義了一個合成(synthesis)分支，用來將兩個分支的回答整合成一個最終的回答。

## 人類參與問答 ([human-in-the-loop.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/human-in-the-loop.ipynb))

製作這樣的Human-in-the-loop系統的動機在於提高LangGraph代理的功能和靈活性。通過添加人在迴圈組件，可以將人類的智慧和判斷力融入到代理的決策過程中，從而提高系統的智能和適應性。

## 入門 ([introduction.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/introduction.ipynb))

建立一個支援型聊天機器人。通過這個教程，使用者可以了解如何使用LangGraph的各種功能和概念，從而建立一個具有基本到複雜功能的聊天機器人。

## 有記憶能儲存狀態 ([persistence.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/persistence.ipynb))

持久性的LangGraph代理的動機在於提供更具交互性和個性化的使用體驗。通過使代理能夠記住之前的互動，使用者可以在多次交互中建立連貫的對話，從而更深入地探索主題或解決問題。

## 儲存到postgres ([persistence_postgres.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/persistence_postgres.ipynb))

狀態存儲到Postgres等持久性後端，可以確保代理在不同交互之間保持連貫的狀態

## Pydantic合規性驗證 ([state-model.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/state-model.ipynb))

Pydantic模型，我們可以定義和驗證代理的狀態，從而確保代理在各個節點的執行過程中始終處於一致和有效的狀態。

## streaming [streaming-tokens.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/streaming-tokens.ipynb)

流式傳輸標記，代理可以立即處理用戶的輸入，實現即時互動和即時回應

## 大圖當中有小圖、可重用 ([subgraph.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/subgraph.ipynb))

子圖（Subgraphs）的動機在於讓我們可以建立更複雜的系統，例如多代理團隊，其中每個團隊可以跟踪自己的狀態，並具有自己的行為和邏輯。通過使用子圖，我們可以將大型系統分解為更小的、可管理的組件。

## 狀態紀錄與回放 ([time-travel.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/time-travel.ipynb))

任何時間點獲取或更新代理的狀態。暫停與更新狀態： 文章示範了如何在執行過程中暫停，以及如何更新狀態並恢復執行。狀態歷史記錄： 最後，文章展示了如何瀏覽和回放對話中的狀態歷史記錄。

## 先建立推理計畫、才去解題 ([self-discover.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/self-discover/self-discover.ipynb))

達成Self-Discover論文的例子，其動機是建立一個系統化的方法，使解題者能夠有效理解問題並找到正確的解答。這個方法包括選擇關鍵的思考模組、將這些模組適應到特定任務上，並建立一個明確的步驟性推理計畫，讓解題者能夠按照這個計畫逐步理解問題並得出結論。

解決一個幾何形狀辨識的問題。具體來說，給定了一個 SVG 路徑元素的描述，需要通過分析該路徑元素的命令和座標，來判斷這個路徑元素所畫的是哪種幾何形狀。這個問題需要應用多個推理模塊，如詳細的路徑分析、路徑分解、SVG 系統分析、命令解釋和幾何推理等，以及結構化的推理計劃，來準確識別給定的形狀。
