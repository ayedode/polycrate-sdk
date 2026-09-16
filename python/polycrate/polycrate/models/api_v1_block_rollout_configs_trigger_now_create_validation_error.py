from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_block_rollout_configs_trigger_now_create_action_name_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateActionNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_active_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateActiveErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_actual_availability_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_annotations_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_archived_at_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_archived_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateArchivedErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_archived_reason_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_auto_takeover_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateAutoTakeoverErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_block_config_template_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateBlockConfigTemplateErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_block_name_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateBlockNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_bypass_maintenance_window_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateBypassMaintenanceWindowErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_conditions_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateConditionsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_config_to_credential_mappings_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateConfigToCredentialMappingsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_criticality_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_cron_expression_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateCronExpressionErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_debug_mode_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_discovery_enabled_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_discovery_running_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_discovery_task_id_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_discovery_task_meta_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_display_name_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_enqueue_reason_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateEnqueueReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_failure_threshold_percent_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateFailureThresholdPercentErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_is_system_config_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateIsSystemConfigErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_kind_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateKindErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_labels_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateLabelsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_last_state_change_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateLastStateChangeErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_last_state_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateLastStateErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_maintenance_window_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateMaintenanceWindowErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_max_concurrent_percent_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateMaxConcurrentPercentErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_max_retries_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateMaxRetriesErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_name_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_non_field_errors_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_notify_on_wave_blocked_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateNotifyOnWaveBlockedErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_platform_service_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_provider_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateProviderErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_provider_id_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_provider_reference_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_reconciliation_enabled_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_reconciliation_running_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_reconciliation_task_id_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_reconciliation_task_meta_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_repair_running_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateRepairRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_repair_task_id_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateRepairTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_repair_task_meta_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateRepairTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_scope_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateScopeErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_scope_expressions_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateScopeExpressionsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_sla_availability_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_sla_target_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_slo_availability_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_slo_target_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_state_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateStateErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_state_reason_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateStateReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_target_availability_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_target_organizations_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateTargetOrganizationsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_target_version_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateTargetVersionErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_target_workspaces_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateTargetWorkspacesErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_template_block_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateTemplateBlockErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_tolerations_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_trigger_now_create_trigger_type_error_component import (
        ApiV1BlockRolloutConfigsTriggerNowCreateTriggerTypeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlockRolloutConfigsTriggerNowCreateValidationError")


@_attrs_define
class ApiV1BlockRolloutConfigsTriggerNowCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlockRolloutConfigsTriggerNowCreateActionNameErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateActiveErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateActualAvailabilityErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateAnnotationsErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateArchivedAtErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateArchivedErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateArchivedReasonErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateAutoTakeoverErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateBlockConfigTemplateErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateBlockNameErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateBypassMaintenanceWindowErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateConditionsErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateConfigToCredentialMappingsErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateCriticalityErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateCronExpressionErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateDebugModeErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryEnabledErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryRunningErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryTaskIdErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryTaskMetaErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateDisplayNameErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateEnqueueReasonErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateFailureThresholdPercentErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateIsSystemConfigErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateKindErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateLabelsErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateLastStateChangeErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateLastStateErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateMaintenanceWindowErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateMaxConcurrentPercentErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateMaxRetriesErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateNameErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateNonFieldErrorsErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateNotifyOnWaveBlockedErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreatePlatformServiceErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateProviderErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateProviderIdErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateProviderReferenceErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationEnabledErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationRunningErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationTaskIdErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationTaskMetaErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateRepairRunningErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateRepairTaskIdErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateRepairTaskMetaErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateScopeErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateScopeExpressionsErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateSlaAvailabilityErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateSlaTargetErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateSloAvailabilityErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateSloTargetErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateStateErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateStateReasonErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateTargetAvailabilityErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateTargetOrganizationsErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateTargetVersionErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateTargetWorkspacesErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateTemplateBlockErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateTolerationsErrorComponent |
            ApiV1BlockRolloutConfigsTriggerNowCreateTriggerTypeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlockRolloutConfigsTriggerNowCreateActionNameErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateActiveErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateActualAvailabilityErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateAnnotationsErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateArchivedAtErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateArchivedErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateArchivedReasonErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateAutoTakeoverErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateBlockConfigTemplateErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateBlockNameErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateBypassMaintenanceWindowErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateConditionsErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateConfigToCredentialMappingsErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateCriticalityErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateCronExpressionErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateDebugModeErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryEnabledErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryRunningErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryTaskIdErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryTaskMetaErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateDisplayNameErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateEnqueueReasonErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateFailureThresholdPercentErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateIsSystemConfigErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateKindErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateLabelsErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateLastStateChangeErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateLastStateErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateMaintenanceWindowErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateMaxConcurrentPercentErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateMaxRetriesErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateNameErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateNonFieldErrorsErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateNotifyOnWaveBlockedErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreatePlatformServiceErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateProviderErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateProviderIdErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateProviderReferenceErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationEnabledErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationRunningErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationTaskIdErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationTaskMetaErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateRepairRunningErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateRepairTaskIdErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateRepairTaskMetaErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateScopeErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateScopeExpressionsErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateSlaAvailabilityErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateSlaTargetErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateSloAvailabilityErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateSloTargetErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateStateErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateStateReasonErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateTargetAvailabilityErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateTargetOrganizationsErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateTargetVersionErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateTargetWorkspacesErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateTemplateBlockErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateTolerationsErrorComponent
        | ApiV1BlockRolloutConfigsTriggerNowCreateTriggerTypeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_block_rollout_configs_trigger_now_create_action_name_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateActionNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_active_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_actual_availability_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_annotations_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_archived_at_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_archived_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_archived_reason_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_auto_takeover_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateAutoTakeoverErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_block_config_template_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateBlockConfigTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_block_name_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateBlockNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_bypass_maintenance_window_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateBypassMaintenanceWindowErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_conditions_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateConditionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_config_to_credential_mappings_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateConfigToCredentialMappingsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_criticality_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_cron_expression_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateCronExpressionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_debug_mode_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_discovery_enabled_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_discovery_running_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_discovery_task_id_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_discovery_task_meta_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_display_name_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_enqueue_reason_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateEnqueueReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_failure_threshold_percent_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateFailureThresholdPercentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_is_system_config_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateIsSystemConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_kind_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_labels_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_last_state_change_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateLastStateChangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_last_state_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateLastStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_maintenance_window_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateMaintenanceWindowErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_max_concurrent_percent_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateMaxConcurrentPercentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_max_retries_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateMaxRetriesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_name_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_non_field_errors_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_platform_service_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_provider_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_provider_id_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_provider_reference_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_reconciliation_running_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_repair_running_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateRepairRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_repair_task_id_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateRepairTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_repair_task_meta_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateRepairTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_scope_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_scope_expressions_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateScopeExpressionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_sla_availability_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_sla_target_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_slo_availability_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_slo_target_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_state_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_state_reason_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateStateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_target_availability_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_target_organizations_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateTargetOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_target_version_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateTargetVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_target_workspaces_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateTargetWorkspacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_template_block_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateTemplateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_tolerations_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_trigger_type_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateTriggerTypeErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateStateReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateLastStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateLastStateChangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationRunningErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationTaskIdErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationTaskMetaErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateRepairRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateRepairTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateRepairTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateConditionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateBlockNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateIsSystemConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateTriggerTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateCronExpressionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateActionNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateTargetVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateTemplateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateEnqueueReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateBlockConfigTemplateErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateScopeExpressionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateAutoTakeoverErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateConfigToCredentialMappingsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateTargetOrganizationsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateTargetWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateMaxConcurrentPercentErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateFailureThresholdPercentErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateMaxRetriesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateMaintenanceWindowErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1BlockRolloutConfigsTriggerNowCreateBypassMaintenanceWindowErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_block_rollout_configs_trigger_now_create_action_name_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateActionNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_active_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_actual_availability_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_annotations_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_archived_at_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_archived_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_archived_reason_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_auto_takeover_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateAutoTakeoverErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_block_config_template_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateBlockConfigTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_block_name_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateBlockNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_bypass_maintenance_window_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateBypassMaintenanceWindowErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_conditions_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateConditionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_config_to_credential_mappings_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateConfigToCredentialMappingsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_criticality_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_cron_expression_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateCronExpressionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_debug_mode_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_discovery_enabled_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_discovery_running_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_discovery_task_id_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_discovery_task_meta_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_display_name_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_enqueue_reason_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateEnqueueReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_failure_threshold_percent_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateFailureThresholdPercentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_is_system_config_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateIsSystemConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_kind_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_labels_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_last_state_change_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateLastStateChangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_last_state_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateLastStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_maintenance_window_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateMaintenanceWindowErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_max_concurrent_percent_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateMaxConcurrentPercentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_max_retries_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateMaxRetriesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_name_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_non_field_errors_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_notify_on_wave_blocked_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateNotifyOnWaveBlockedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_platform_service_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_provider_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_provider_id_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_provider_reference_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_reconciliation_running_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_repair_running_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateRepairRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_repair_task_id_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateRepairTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_repair_task_meta_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateRepairTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_scope_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_scope_expressions_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateScopeExpressionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_sla_availability_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_sla_target_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_slo_availability_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_slo_target_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_state_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_state_reason_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateStateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_target_availability_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_target_organizations_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateTargetOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_target_version_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateTargetVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_target_workspaces_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateTargetWorkspacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_template_block_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateTemplateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_tolerations_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_trigger_now_create_trigger_type_error_component import (
            ApiV1BlockRolloutConfigsTriggerNowCreateTriggerTypeErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlockRolloutConfigsTriggerNowCreateActionNameErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateActiveErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateActualAvailabilityErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateAnnotationsErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateArchivedAtErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateArchivedErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateArchivedReasonErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateAutoTakeoverErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateBlockConfigTemplateErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateBlockNameErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateBypassMaintenanceWindowErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateConditionsErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateConfigToCredentialMappingsErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateCriticalityErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateCronExpressionErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateDebugModeErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryEnabledErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryRunningErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryTaskIdErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryTaskMetaErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateDisplayNameErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateEnqueueReasonErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateFailureThresholdPercentErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateIsSystemConfigErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateKindErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateLabelsErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateLastStateChangeErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateLastStateErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateMaintenanceWindowErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateMaxConcurrentPercentErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateMaxRetriesErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateNameErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateNonFieldErrorsErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateNotifyOnWaveBlockedErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreatePlatformServiceErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateProviderErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateProviderIdErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateProviderReferenceErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationEnabledErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationRunningErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationTaskIdErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationTaskMetaErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateRepairRunningErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateRepairTaskIdErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateRepairTaskMetaErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateScopeErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateScopeExpressionsErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateSlaAvailabilityErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateSlaTargetErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateSloAvailabilityErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateSloTargetErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateStateErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateStateReasonErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateTargetAvailabilityErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateTargetOrganizationsErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateTargetVersionErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateTargetWorkspacesErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateTemplateBlockErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateTolerationsErrorComponent
                | ApiV1BlockRolloutConfigsTriggerNowCreateTriggerTypeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_0 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_1 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_2 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_3 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_4 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_5 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_6 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_7 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_8 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_9 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_10 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateStateReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_11 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateLastStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_12 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateLastStateChangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_13 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_14 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_15 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_16 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateReconciliationTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_17 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_18 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_19 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_20 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateDiscoveryTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_21 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateRepairRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_22 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_23 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateRepairTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_24 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateRepairTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_25 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_26 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_27 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateConditionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_28 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_29 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_30 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_31 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_32 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_33 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_34 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_35 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_36 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_37 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_38 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_39 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateBlockNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_40 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_41 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateIsSystemConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_42 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateTriggerTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_43 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateCronExpressionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_44 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateActionNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_45 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateTargetVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_46 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateTemplateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_47 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateEnqueueReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_48 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateBlockConfigTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_49 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateScopeExpressionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_50 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateAutoTakeoverErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_51 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateConfigToCredentialMappingsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_52 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateTargetOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_53 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateTargetWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_54 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateMaxConcurrentPercentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_55 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateFailureThresholdPercentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_56 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateMaxRetriesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_57 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateMaintenanceWindowErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_58 = (
                        ApiV1BlockRolloutConfigsTriggerNowCreateBypassMaintenanceWindowErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_59 = (
                    ApiV1BlockRolloutConfigsTriggerNowCreateNotifyOnWaveBlockedErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_block_rollout_configs_trigger_now_create_error_type_59

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_block_rollout_configs_trigger_now_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_block_rollout_configs_trigger_now_create_validation_error.additional_properties = d
        return api_v1_block_rollout_configs_trigger_now_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
