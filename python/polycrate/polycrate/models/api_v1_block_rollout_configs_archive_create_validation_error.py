from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_block_rollout_configs_archive_create_action_name_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateActionNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_active_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateActiveErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_actual_availability_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_annotations_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_archived_at_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_archived_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_archived_reason_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_auto_takeover_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateAutoTakeoverErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_block_config_template_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateBlockConfigTemplateErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_block_name_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateBlockNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_bypass_maintenance_window_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateBypassMaintenanceWindowErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_conditions_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateConditionsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_config_to_credential_mappings_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateConfigToCredentialMappingsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_criticality_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_cron_expression_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateCronExpressionErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_debug_mode_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_discovery_enabled_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_discovery_running_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateDiscoveryRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_discovery_task_id_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateDiscoveryTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_discovery_task_meta_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateDiscoveryTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_display_name_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_enqueue_reason_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateEnqueueReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_failure_threshold_percent_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateFailureThresholdPercentErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_is_system_config_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateIsSystemConfigErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_kind_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_labels_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_last_state_change_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateLastStateChangeErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_last_state_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateLastStateErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_maintenance_window_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateMaintenanceWindowErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_max_concurrent_percent_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateMaxConcurrentPercentErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_max_retries_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateMaxRetriesErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_name_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_non_field_errors_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_notify_on_wave_blocked_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateNotifyOnWaveBlockedErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_platform_service_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_provider_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_provider_id_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_provider_reference_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_reconciliation_enabled_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_reconciliation_running_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateReconciliationRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_reconciliation_task_id_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateReconciliationTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_reconciliation_task_meta_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateReconciliationTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_repair_running_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateRepairRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_repair_task_id_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateRepairTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_repair_task_meta_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateRepairTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_scope_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateScopeErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_scope_expressions_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateScopeExpressionsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_sla_availability_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_sla_target_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_slo_availability_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_slo_target_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_state_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateStateErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_state_reason_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateStateReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_target_availability_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_target_organizations_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateTargetOrganizationsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_target_version_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateTargetVersionErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_target_workspaces_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateTargetWorkspacesErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_template_block_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateTemplateBlockErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_tolerations_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_block_rollout_configs_archive_create_trigger_type_error_component import (
        ApiV1BlockRolloutConfigsArchiveCreateTriggerTypeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlockRolloutConfigsArchiveCreateValidationError")


@_attrs_define
class ApiV1BlockRolloutConfigsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlockRolloutConfigsArchiveCreateActionNameErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateActiveErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateActualAvailabilityErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateAnnotationsErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateArchivedAtErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateArchivedErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateArchivedReasonErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateAutoTakeoverErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateBlockConfigTemplateErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateBlockNameErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateBypassMaintenanceWindowErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateConditionsErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateConfigToCredentialMappingsErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateCriticalityErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateCronExpressionErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateDebugModeErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateDiscoveryEnabledErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateDiscoveryRunningErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateDiscoveryTaskIdErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateDiscoveryTaskMetaErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateDisplayNameErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateEnqueueReasonErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateFailureThresholdPercentErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateIsSystemConfigErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateKindErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateLabelsErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateLastStateChangeErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateLastStateErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateMaintenanceWindowErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateMaxConcurrentPercentErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateMaxRetriesErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateNameErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateNotifyOnWaveBlockedErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreatePlatformServiceErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateProviderErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateProviderIdErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateProviderReferenceErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateReconciliationRunningErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateReconciliationTaskIdErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateReconciliationTaskMetaErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateRepairRunningErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateRepairTaskIdErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateRepairTaskMetaErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateScopeErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateScopeExpressionsErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateSlaTargetErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateSloTargetErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateStateErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateStateReasonErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateTargetOrganizationsErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateTargetVersionErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateTargetWorkspacesErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateTemplateBlockErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateTolerationsErrorComponent |
            ApiV1BlockRolloutConfigsArchiveCreateTriggerTypeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlockRolloutConfigsArchiveCreateActionNameErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateActiveErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateActualAvailabilityErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateAnnotationsErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateArchivedAtErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateArchivedErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateArchivedReasonErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateAutoTakeoverErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateBlockConfigTemplateErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateBlockNameErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateBypassMaintenanceWindowErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateConditionsErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateConfigToCredentialMappingsErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateCriticalityErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateCronExpressionErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateDebugModeErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateDiscoveryEnabledErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateDiscoveryRunningErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateDiscoveryTaskIdErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateDiscoveryTaskMetaErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateDisplayNameErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateEnqueueReasonErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateFailureThresholdPercentErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateIsSystemConfigErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateKindErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateLabelsErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateLastStateChangeErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateLastStateErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateMaintenanceWindowErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateMaxConcurrentPercentErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateMaxRetriesErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateNameErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateNotifyOnWaveBlockedErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreatePlatformServiceErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateProviderErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateProviderIdErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateProviderReferenceErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateReconciliationRunningErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateReconciliationTaskIdErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateReconciliationTaskMetaErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateRepairRunningErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateRepairTaskIdErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateRepairTaskMetaErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateScopeErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateScopeExpressionsErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateSlaTargetErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateSloTargetErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateStateErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateStateReasonErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateTargetOrganizationsErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateTargetVersionErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateTargetWorkspacesErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateTemplateBlockErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateTolerationsErrorComponent
        | ApiV1BlockRolloutConfigsArchiveCreateTriggerTypeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_block_rollout_configs_archive_create_action_name_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateActionNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_active_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_actual_availability_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_annotations_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_archived_at_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_archived_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_archived_reason_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_auto_takeover_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateAutoTakeoverErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_block_config_template_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateBlockConfigTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_block_name_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateBlockNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_bypass_maintenance_window_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateBypassMaintenanceWindowErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_conditions_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateConditionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_config_to_credential_mappings_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateConfigToCredentialMappingsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_criticality_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_cron_expression_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateCronExpressionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_debug_mode_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_discovery_enabled_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_discovery_running_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateDiscoveryRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_discovery_task_id_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateDiscoveryTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_discovery_task_meta_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateDiscoveryTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_display_name_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_enqueue_reason_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateEnqueueReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_failure_threshold_percent_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateFailureThresholdPercentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_is_system_config_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateIsSystemConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_kind_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_labels_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_last_state_change_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateLastStateChangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_last_state_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateLastStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_maintenance_window_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateMaintenanceWindowErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_max_concurrent_percent_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateMaxConcurrentPercentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_max_retries_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateMaxRetriesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_name_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_non_field_errors_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_platform_service_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_provider_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_provider_id_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_provider_reference_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_reconciliation_running_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateReconciliationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateReconciliationTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateReconciliationTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_repair_running_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateRepairRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_repair_task_id_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateRepairTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_repair_task_meta_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateRepairTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_scope_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_scope_expressions_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateScopeExpressionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_sla_availability_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_sla_target_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_slo_availability_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_slo_target_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_state_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_state_reason_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateStateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_target_availability_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_target_organizations_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateTargetOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_target_version_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateTargetVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_target_workspaces_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateTargetWorkspacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_template_block_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateTemplateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_tolerations_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_trigger_type_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateTriggerTypeErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateStateReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateLastStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateLastStateChangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateReconciliationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateReconciliationTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateReconciliationTaskMetaErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateDiscoveryRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateDiscoveryTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateDiscoveryTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateRepairRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateRepairTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateRepairTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateConditionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateBlockNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateIsSystemConfigErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateTriggerTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateCronExpressionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateActionNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateTargetVersionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateTemplateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateEnqueueReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateBlockConfigTemplateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateScopeExpressionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateAutoTakeoverErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateConfigToCredentialMappingsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateTargetOrganizationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateTargetWorkspacesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateMaxConcurrentPercentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateFailureThresholdPercentErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateMaxRetriesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateMaintenanceWindowErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1BlockRolloutConfigsArchiveCreateBypassMaintenanceWindowErrorComponent
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
        from ..models.api_v1_block_rollout_configs_archive_create_action_name_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateActionNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_active_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_actual_availability_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_annotations_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_archived_at_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_archived_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_archived_reason_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_auto_takeover_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateAutoTakeoverErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_block_config_template_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateBlockConfigTemplateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_block_name_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateBlockNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_bypass_maintenance_window_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateBypassMaintenanceWindowErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_conditions_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateConditionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_config_to_credential_mappings_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateConfigToCredentialMappingsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_criticality_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_cron_expression_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateCronExpressionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_debug_mode_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_discovery_enabled_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_discovery_running_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateDiscoveryRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_discovery_task_id_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateDiscoveryTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_discovery_task_meta_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateDiscoveryTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_display_name_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_enqueue_reason_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateEnqueueReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_failure_threshold_percent_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateFailureThresholdPercentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_is_system_config_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateIsSystemConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_kind_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_labels_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_last_state_change_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateLastStateChangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_last_state_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateLastStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_maintenance_window_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateMaintenanceWindowErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_max_concurrent_percent_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateMaxConcurrentPercentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_max_retries_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateMaxRetriesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_name_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_non_field_errors_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_notify_on_wave_blocked_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateNotifyOnWaveBlockedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_platform_service_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_provider_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_provider_id_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_provider_reference_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_reconciliation_running_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateReconciliationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateReconciliationTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateReconciliationTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_repair_running_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateRepairRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_repair_task_id_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateRepairTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_repair_task_meta_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateRepairTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_scope_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_scope_expressions_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateScopeExpressionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_sla_availability_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_sla_target_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_slo_availability_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_slo_target_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_state_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_state_reason_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateStateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_target_availability_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_target_organizations_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateTargetOrganizationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_target_version_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateTargetVersionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_target_workspaces_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateTargetWorkspacesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_template_block_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateTemplateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_tolerations_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_configs_archive_create_trigger_type_error_component import (
            ApiV1BlockRolloutConfigsArchiveCreateTriggerTypeErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlockRolloutConfigsArchiveCreateActionNameErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateActiveErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateActualAvailabilityErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateAnnotationsErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateArchivedAtErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateArchivedErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateArchivedReasonErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateAutoTakeoverErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateBlockConfigTemplateErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateBlockNameErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateBypassMaintenanceWindowErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateConditionsErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateConfigToCredentialMappingsErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateCriticalityErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateCronExpressionErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateDebugModeErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateDiscoveryEnabledErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateDiscoveryRunningErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateDiscoveryTaskIdErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateDiscoveryTaskMetaErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateDisplayNameErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateEnqueueReasonErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateFailureThresholdPercentErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateIsSystemConfigErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateKindErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateLabelsErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateLastStateChangeErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateLastStateErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateMaintenanceWindowErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateMaxConcurrentPercentErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateMaxRetriesErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateNameErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateNotifyOnWaveBlockedErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreatePlatformServiceErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateProviderErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateProviderIdErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateProviderReferenceErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateReconciliationRunningErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateReconciliationTaskIdErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateReconciliationTaskMetaErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateRepairRunningErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateRepairTaskIdErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateRepairTaskMetaErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateScopeErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateScopeExpressionsErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateSlaTargetErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateSloTargetErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateStateErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateStateReasonErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateTargetOrganizationsErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateTargetVersionErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateTargetWorkspacesErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateTemplateBlockErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateTolerationsErrorComponent
                | ApiV1BlockRolloutConfigsArchiveCreateTriggerTypeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_0 = (
                        ApiV1BlockRolloutConfigsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_1 = (
                        ApiV1BlockRolloutConfigsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_2 = (
                        ApiV1BlockRolloutConfigsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_3 = (
                        ApiV1BlockRolloutConfigsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_4 = (
                        ApiV1BlockRolloutConfigsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_5 = (
                        ApiV1BlockRolloutConfigsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_6 = (
                        ApiV1BlockRolloutConfigsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_7 = (
                        ApiV1BlockRolloutConfigsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_8 = (
                        ApiV1BlockRolloutConfigsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_9 = (
                        ApiV1BlockRolloutConfigsArchiveCreateStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_10 = (
                        ApiV1BlockRolloutConfigsArchiveCreateStateReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_11 = (
                        ApiV1BlockRolloutConfigsArchiveCreateLastStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_12 = (
                        ApiV1BlockRolloutConfigsArchiveCreateLastStateChangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_13 = (
                        ApiV1BlockRolloutConfigsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_14 = (
                        ApiV1BlockRolloutConfigsArchiveCreateReconciliationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_15 = (
                        ApiV1BlockRolloutConfigsArchiveCreateReconciliationTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_16 = (
                        ApiV1BlockRolloutConfigsArchiveCreateReconciliationTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_17 = (
                        ApiV1BlockRolloutConfigsArchiveCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_18 = (
                        ApiV1BlockRolloutConfigsArchiveCreateDiscoveryRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_19 = (
                        ApiV1BlockRolloutConfigsArchiveCreateDiscoveryTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_20 = (
                        ApiV1BlockRolloutConfigsArchiveCreateDiscoveryTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_21 = (
                        ApiV1BlockRolloutConfigsArchiveCreateRepairRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_22 = (
                        ApiV1BlockRolloutConfigsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_23 = (
                        ApiV1BlockRolloutConfigsArchiveCreateRepairTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_24 = (
                        ApiV1BlockRolloutConfigsArchiveCreateRepairTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_25 = (
                        ApiV1BlockRolloutConfigsArchiveCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_26 = (
                        ApiV1BlockRolloutConfigsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_27 = (
                        ApiV1BlockRolloutConfigsArchiveCreateConditionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_28 = (
                        ApiV1BlockRolloutConfigsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_29 = (
                        ApiV1BlockRolloutConfigsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_30 = (
                        ApiV1BlockRolloutConfigsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_31 = (
                        ApiV1BlockRolloutConfigsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_32 = (
                        ApiV1BlockRolloutConfigsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_33 = (
                        ApiV1BlockRolloutConfigsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_34 = (
                        ApiV1BlockRolloutConfigsArchiveCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_35 = (
                        ApiV1BlockRolloutConfigsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_36 = (
                        ApiV1BlockRolloutConfigsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_37 = (
                        ApiV1BlockRolloutConfigsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_38 = (
                        ApiV1BlockRolloutConfigsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_39 = (
                        ApiV1BlockRolloutConfigsArchiveCreateBlockNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_40 = (
                        ApiV1BlockRolloutConfigsArchiveCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_41 = (
                        ApiV1BlockRolloutConfigsArchiveCreateIsSystemConfigErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_42 = (
                        ApiV1BlockRolloutConfigsArchiveCreateTriggerTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_43 = (
                        ApiV1BlockRolloutConfigsArchiveCreateCronExpressionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_44 = (
                        ApiV1BlockRolloutConfigsArchiveCreateActionNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_45 = (
                        ApiV1BlockRolloutConfigsArchiveCreateTargetVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_46 = (
                        ApiV1BlockRolloutConfigsArchiveCreateTemplateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_47 = (
                        ApiV1BlockRolloutConfigsArchiveCreateEnqueueReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_48 = (
                        ApiV1BlockRolloutConfigsArchiveCreateBlockConfigTemplateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_49 = (
                        ApiV1BlockRolloutConfigsArchiveCreateScopeExpressionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_50 = (
                        ApiV1BlockRolloutConfigsArchiveCreateAutoTakeoverErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_51 = (
                        ApiV1BlockRolloutConfigsArchiveCreateConfigToCredentialMappingsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_52 = (
                        ApiV1BlockRolloutConfigsArchiveCreateTargetOrganizationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_53 = (
                        ApiV1BlockRolloutConfigsArchiveCreateTargetWorkspacesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_54 = (
                        ApiV1BlockRolloutConfigsArchiveCreateMaxConcurrentPercentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_55 = (
                        ApiV1BlockRolloutConfigsArchiveCreateFailureThresholdPercentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_55
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_56 = (
                        ApiV1BlockRolloutConfigsArchiveCreateMaxRetriesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_56
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_57 = (
                        ApiV1BlockRolloutConfigsArchiveCreateMaintenanceWindowErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_57
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_58 = (
                        ApiV1BlockRolloutConfigsArchiveCreateBypassMaintenanceWindowErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_58
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_59 = (
                    ApiV1BlockRolloutConfigsArchiveCreateNotifyOnWaveBlockedErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_block_rollout_configs_archive_create_error_type_59

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_block_rollout_configs_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_block_rollout_configs_archive_create_validation_error.additional_properties = d
        return api_v1_block_rollout_configs_archive_create_validation_error

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
