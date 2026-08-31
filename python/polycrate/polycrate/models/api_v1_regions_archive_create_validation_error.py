from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_regions_archive_create_actual_availability_error_component import (
        ApiV1RegionsArchiveCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_annotations_error_component import (
        ApiV1RegionsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_archived_at_error_component import (
        ApiV1RegionsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_archived_error_component import (
        ApiV1RegionsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_archived_reason_error_component import (
        ApiV1RegionsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_conditions_error_component import (
        ApiV1RegionsArchiveCreateConditionsErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_config_error_component import (
        ApiV1RegionsArchiveCreateConfigErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_criticality_error_component import (
        ApiV1RegionsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_debug_mode_error_component import (
        ApiV1RegionsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_discovery_enabled_error_component import (
        ApiV1RegionsArchiveCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_discovery_running_error_component import (
        ApiV1RegionsArchiveCreateDiscoveryRunningErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_discovery_task_id_error_component import (
        ApiV1RegionsArchiveCreateDiscoveryTaskIdErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_discovery_task_meta_error_component import (
        ApiV1RegionsArchiveCreateDiscoveryTaskMetaErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_display_name_error_component import (
        ApiV1RegionsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_kind_error_component import ApiV1RegionsArchiveCreateKindErrorComponent
    from ..models.api_v1_regions_archive_create_labels_error_component import (
        ApiV1RegionsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_last_state_change_error_component import (
        ApiV1RegionsArchiveCreateLastStateChangeErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_last_state_error_component import (
        ApiV1RegionsArchiveCreateLastStateErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_name_error_component import ApiV1RegionsArchiveCreateNameErrorComponent
    from ..models.api_v1_regions_archive_create_non_field_errors_error_component import (
        ApiV1RegionsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_platform_features_error_component import (
        ApiV1RegionsArchiveCreatePlatformFeaturesErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_platform_features_index_error_component import (
        ApiV1RegionsArchiveCreatePlatformFeaturesINDEXErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_platform_service_error_component import (
        ApiV1RegionsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_provider_error_component import (
        ApiV1RegionsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_provider_id_error_component import (
        ApiV1RegionsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_provider_reference_error_component import (
        ApiV1RegionsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_reconciliation_enabled_error_component import (
        ApiV1RegionsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_reconciliation_running_error_component import (
        ApiV1RegionsArchiveCreateReconciliationRunningErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_reconciliation_task_id_error_component import (
        ApiV1RegionsArchiveCreateReconciliationTaskIdErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_reconciliation_task_meta_error_component import (
        ApiV1RegionsArchiveCreateReconciliationTaskMetaErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_repair_running_error_component import (
        ApiV1RegionsArchiveCreateRepairRunningErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_repair_task_id_error_component import (
        ApiV1RegionsArchiveCreateRepairTaskIdErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_repair_task_meta_error_component import (
        ApiV1RegionsArchiveCreateRepairTaskMetaErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_scope_error_component import (
        ApiV1RegionsArchiveCreateScopeErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_sla_availability_error_component import (
        ApiV1RegionsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_sla_target_error_component import (
        ApiV1RegionsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_slo_availability_error_component import (
        ApiV1RegionsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_slo_target_error_component import (
        ApiV1RegionsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_state_error_component import (
        ApiV1RegionsArchiveCreateStateErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_state_reason_error_component import (
        ApiV1RegionsArchiveCreateStateReasonErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_target_availability_error_component import (
        ApiV1RegionsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_regions_archive_create_tolerations_error_component import (
        ApiV1RegionsArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1RegionsArchiveCreateValidationError")


@_attrs_define
class ApiV1RegionsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1RegionsArchiveCreateActualAvailabilityErrorComponent |
            ApiV1RegionsArchiveCreateAnnotationsErrorComponent | ApiV1RegionsArchiveCreateArchivedAtErrorComponent |
            ApiV1RegionsArchiveCreateArchivedErrorComponent | ApiV1RegionsArchiveCreateArchivedReasonErrorComponent |
            ApiV1RegionsArchiveCreateConditionsErrorComponent | ApiV1RegionsArchiveCreateConfigErrorComponent |
            ApiV1RegionsArchiveCreateCriticalityErrorComponent | ApiV1RegionsArchiveCreateDebugModeErrorComponent |
            ApiV1RegionsArchiveCreateDiscoveryEnabledErrorComponent |
            ApiV1RegionsArchiveCreateDiscoveryRunningErrorComponent | ApiV1RegionsArchiveCreateDiscoveryTaskIdErrorComponent
            | ApiV1RegionsArchiveCreateDiscoveryTaskMetaErrorComponent | ApiV1RegionsArchiveCreateDisplayNameErrorComponent
            | ApiV1RegionsArchiveCreateKindErrorComponent | ApiV1RegionsArchiveCreateLabelsErrorComponent |
            ApiV1RegionsArchiveCreateLastStateChangeErrorComponent | ApiV1RegionsArchiveCreateLastStateErrorComponent |
            ApiV1RegionsArchiveCreateNameErrorComponent | ApiV1RegionsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1RegionsArchiveCreatePlatformFeaturesErrorComponent |
            ApiV1RegionsArchiveCreatePlatformFeaturesINDEXErrorComponent |
            ApiV1RegionsArchiveCreatePlatformServiceErrorComponent | ApiV1RegionsArchiveCreateProviderErrorComponent |
            ApiV1RegionsArchiveCreateProviderIdErrorComponent | ApiV1RegionsArchiveCreateProviderReferenceErrorComponent |
            ApiV1RegionsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1RegionsArchiveCreateReconciliationRunningErrorComponent |
            ApiV1RegionsArchiveCreateReconciliationTaskIdErrorComponent |
            ApiV1RegionsArchiveCreateReconciliationTaskMetaErrorComponent |
            ApiV1RegionsArchiveCreateRepairRunningErrorComponent | ApiV1RegionsArchiveCreateRepairTaskIdErrorComponent |
            ApiV1RegionsArchiveCreateRepairTaskMetaErrorComponent | ApiV1RegionsArchiveCreateScopeErrorComponent |
            ApiV1RegionsArchiveCreateSlaAvailabilityErrorComponent | ApiV1RegionsArchiveCreateSlaTargetErrorComponent |
            ApiV1RegionsArchiveCreateSloAvailabilityErrorComponent | ApiV1RegionsArchiveCreateSloTargetErrorComponent |
            ApiV1RegionsArchiveCreateStateErrorComponent | ApiV1RegionsArchiveCreateStateReasonErrorComponent |
            ApiV1RegionsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1RegionsArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1RegionsArchiveCreateActualAvailabilityErrorComponent
        | ApiV1RegionsArchiveCreateAnnotationsErrorComponent
        | ApiV1RegionsArchiveCreateArchivedAtErrorComponent
        | ApiV1RegionsArchiveCreateArchivedErrorComponent
        | ApiV1RegionsArchiveCreateArchivedReasonErrorComponent
        | ApiV1RegionsArchiveCreateConditionsErrorComponent
        | ApiV1RegionsArchiveCreateConfigErrorComponent
        | ApiV1RegionsArchiveCreateCriticalityErrorComponent
        | ApiV1RegionsArchiveCreateDebugModeErrorComponent
        | ApiV1RegionsArchiveCreateDiscoveryEnabledErrorComponent
        | ApiV1RegionsArchiveCreateDiscoveryRunningErrorComponent
        | ApiV1RegionsArchiveCreateDiscoveryTaskIdErrorComponent
        | ApiV1RegionsArchiveCreateDiscoveryTaskMetaErrorComponent
        | ApiV1RegionsArchiveCreateDisplayNameErrorComponent
        | ApiV1RegionsArchiveCreateKindErrorComponent
        | ApiV1RegionsArchiveCreateLabelsErrorComponent
        | ApiV1RegionsArchiveCreateLastStateChangeErrorComponent
        | ApiV1RegionsArchiveCreateLastStateErrorComponent
        | ApiV1RegionsArchiveCreateNameErrorComponent
        | ApiV1RegionsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1RegionsArchiveCreatePlatformFeaturesErrorComponent
        | ApiV1RegionsArchiveCreatePlatformFeaturesINDEXErrorComponent
        | ApiV1RegionsArchiveCreatePlatformServiceErrorComponent
        | ApiV1RegionsArchiveCreateProviderErrorComponent
        | ApiV1RegionsArchiveCreateProviderIdErrorComponent
        | ApiV1RegionsArchiveCreateProviderReferenceErrorComponent
        | ApiV1RegionsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1RegionsArchiveCreateReconciliationRunningErrorComponent
        | ApiV1RegionsArchiveCreateReconciliationTaskIdErrorComponent
        | ApiV1RegionsArchiveCreateReconciliationTaskMetaErrorComponent
        | ApiV1RegionsArchiveCreateRepairRunningErrorComponent
        | ApiV1RegionsArchiveCreateRepairTaskIdErrorComponent
        | ApiV1RegionsArchiveCreateRepairTaskMetaErrorComponent
        | ApiV1RegionsArchiveCreateScopeErrorComponent
        | ApiV1RegionsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1RegionsArchiveCreateSlaTargetErrorComponent
        | ApiV1RegionsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1RegionsArchiveCreateSloTargetErrorComponent
        | ApiV1RegionsArchiveCreateStateErrorComponent
        | ApiV1RegionsArchiveCreateStateReasonErrorComponent
        | ApiV1RegionsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1RegionsArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_regions_archive_create_actual_availability_error_component import (
            ApiV1RegionsArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_annotations_error_component import (
            ApiV1RegionsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_archived_at_error_component import (
            ApiV1RegionsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_archived_error_component import (
            ApiV1RegionsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_archived_reason_error_component import (
            ApiV1RegionsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_conditions_error_component import (
            ApiV1RegionsArchiveCreateConditionsErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_criticality_error_component import (
            ApiV1RegionsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_debug_mode_error_component import (
            ApiV1RegionsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_discovery_enabled_error_component import (
            ApiV1RegionsArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_discovery_running_error_component import (
            ApiV1RegionsArchiveCreateDiscoveryRunningErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_discovery_task_id_error_component import (
            ApiV1RegionsArchiveCreateDiscoveryTaskIdErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_discovery_task_meta_error_component import (
            ApiV1RegionsArchiveCreateDiscoveryTaskMetaErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_display_name_error_component import (
            ApiV1RegionsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_kind_error_component import (
            ApiV1RegionsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_labels_error_component import (
            ApiV1RegionsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_last_state_change_error_component import (
            ApiV1RegionsArchiveCreateLastStateChangeErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_last_state_error_component import (
            ApiV1RegionsArchiveCreateLastStateErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_name_error_component import (
            ApiV1RegionsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_non_field_errors_error_component import (
            ApiV1RegionsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_platform_features_error_component import (
            ApiV1RegionsArchiveCreatePlatformFeaturesErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_platform_features_index_error_component import (
            ApiV1RegionsArchiveCreatePlatformFeaturesINDEXErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_platform_service_error_component import (
            ApiV1RegionsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_provider_error_component import (
            ApiV1RegionsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_provider_id_error_component import (
            ApiV1RegionsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_provider_reference_error_component import (
            ApiV1RegionsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_reconciliation_enabled_error_component import (
            ApiV1RegionsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_reconciliation_running_error_component import (
            ApiV1RegionsArchiveCreateReconciliationRunningErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_reconciliation_task_id_error_component import (
            ApiV1RegionsArchiveCreateReconciliationTaskIdErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_reconciliation_task_meta_error_component import (
            ApiV1RegionsArchiveCreateReconciliationTaskMetaErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_repair_running_error_component import (
            ApiV1RegionsArchiveCreateRepairRunningErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_repair_task_id_error_component import (
            ApiV1RegionsArchiveCreateRepairTaskIdErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_repair_task_meta_error_component import (
            ApiV1RegionsArchiveCreateRepairTaskMetaErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_scope_error_component import (
            ApiV1RegionsArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_sla_availability_error_component import (
            ApiV1RegionsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_sla_target_error_component import (
            ApiV1RegionsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_slo_availability_error_component import (
            ApiV1RegionsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_slo_target_error_component import (
            ApiV1RegionsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_state_error_component import (
            ApiV1RegionsArchiveCreateStateErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_state_reason_error_component import (
            ApiV1RegionsArchiveCreateStateReasonErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_target_availability_error_component import (
            ApiV1RegionsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_tolerations_error_component import (
            ApiV1RegionsArchiveCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1RegionsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateStateReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateLastStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateLastStateChangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateReconciliationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateReconciliationTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateReconciliationTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateDiscoveryRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateDiscoveryTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateDiscoveryTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateRepairRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateRepairTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateRepairTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateConditionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreatePlatformFeaturesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsArchiveCreatePlatformFeaturesINDEXErrorComponent):
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
        from ..models.api_v1_regions_archive_create_actual_availability_error_component import (
            ApiV1RegionsArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_annotations_error_component import (
            ApiV1RegionsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_archived_at_error_component import (
            ApiV1RegionsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_archived_error_component import (
            ApiV1RegionsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_archived_reason_error_component import (
            ApiV1RegionsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_conditions_error_component import (
            ApiV1RegionsArchiveCreateConditionsErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_config_error_component import (
            ApiV1RegionsArchiveCreateConfigErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_criticality_error_component import (
            ApiV1RegionsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_debug_mode_error_component import (
            ApiV1RegionsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_discovery_enabled_error_component import (
            ApiV1RegionsArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_discovery_running_error_component import (
            ApiV1RegionsArchiveCreateDiscoveryRunningErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_discovery_task_id_error_component import (
            ApiV1RegionsArchiveCreateDiscoveryTaskIdErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_discovery_task_meta_error_component import (
            ApiV1RegionsArchiveCreateDiscoveryTaskMetaErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_display_name_error_component import (
            ApiV1RegionsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_kind_error_component import (
            ApiV1RegionsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_labels_error_component import (
            ApiV1RegionsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_last_state_change_error_component import (
            ApiV1RegionsArchiveCreateLastStateChangeErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_last_state_error_component import (
            ApiV1RegionsArchiveCreateLastStateErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_name_error_component import (
            ApiV1RegionsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_non_field_errors_error_component import (
            ApiV1RegionsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_platform_features_error_component import (
            ApiV1RegionsArchiveCreatePlatformFeaturesErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_platform_features_index_error_component import (
            ApiV1RegionsArchiveCreatePlatformFeaturesINDEXErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_platform_service_error_component import (
            ApiV1RegionsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_provider_error_component import (
            ApiV1RegionsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_provider_id_error_component import (
            ApiV1RegionsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_provider_reference_error_component import (
            ApiV1RegionsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_reconciliation_enabled_error_component import (
            ApiV1RegionsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_reconciliation_running_error_component import (
            ApiV1RegionsArchiveCreateReconciliationRunningErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_reconciliation_task_id_error_component import (
            ApiV1RegionsArchiveCreateReconciliationTaskIdErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_reconciliation_task_meta_error_component import (
            ApiV1RegionsArchiveCreateReconciliationTaskMetaErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_repair_running_error_component import (
            ApiV1RegionsArchiveCreateRepairRunningErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_repair_task_id_error_component import (
            ApiV1RegionsArchiveCreateRepairTaskIdErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_repair_task_meta_error_component import (
            ApiV1RegionsArchiveCreateRepairTaskMetaErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_scope_error_component import (
            ApiV1RegionsArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_sla_availability_error_component import (
            ApiV1RegionsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_sla_target_error_component import (
            ApiV1RegionsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_slo_availability_error_component import (
            ApiV1RegionsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_slo_target_error_component import (
            ApiV1RegionsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_state_error_component import (
            ApiV1RegionsArchiveCreateStateErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_state_reason_error_component import (
            ApiV1RegionsArchiveCreateStateReasonErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_target_availability_error_component import (
            ApiV1RegionsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_archive_create_tolerations_error_component import (
            ApiV1RegionsArchiveCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1RegionsArchiveCreateActualAvailabilityErrorComponent
                | ApiV1RegionsArchiveCreateAnnotationsErrorComponent
                | ApiV1RegionsArchiveCreateArchivedAtErrorComponent
                | ApiV1RegionsArchiveCreateArchivedErrorComponent
                | ApiV1RegionsArchiveCreateArchivedReasonErrorComponent
                | ApiV1RegionsArchiveCreateConditionsErrorComponent
                | ApiV1RegionsArchiveCreateConfigErrorComponent
                | ApiV1RegionsArchiveCreateCriticalityErrorComponent
                | ApiV1RegionsArchiveCreateDebugModeErrorComponent
                | ApiV1RegionsArchiveCreateDiscoveryEnabledErrorComponent
                | ApiV1RegionsArchiveCreateDiscoveryRunningErrorComponent
                | ApiV1RegionsArchiveCreateDiscoveryTaskIdErrorComponent
                | ApiV1RegionsArchiveCreateDiscoveryTaskMetaErrorComponent
                | ApiV1RegionsArchiveCreateDisplayNameErrorComponent
                | ApiV1RegionsArchiveCreateKindErrorComponent
                | ApiV1RegionsArchiveCreateLabelsErrorComponent
                | ApiV1RegionsArchiveCreateLastStateChangeErrorComponent
                | ApiV1RegionsArchiveCreateLastStateErrorComponent
                | ApiV1RegionsArchiveCreateNameErrorComponent
                | ApiV1RegionsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1RegionsArchiveCreatePlatformFeaturesErrorComponent
                | ApiV1RegionsArchiveCreatePlatformFeaturesINDEXErrorComponent
                | ApiV1RegionsArchiveCreatePlatformServiceErrorComponent
                | ApiV1RegionsArchiveCreateProviderErrorComponent
                | ApiV1RegionsArchiveCreateProviderIdErrorComponent
                | ApiV1RegionsArchiveCreateProviderReferenceErrorComponent
                | ApiV1RegionsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1RegionsArchiveCreateReconciliationRunningErrorComponent
                | ApiV1RegionsArchiveCreateReconciliationTaskIdErrorComponent
                | ApiV1RegionsArchiveCreateReconciliationTaskMetaErrorComponent
                | ApiV1RegionsArchiveCreateRepairRunningErrorComponent
                | ApiV1RegionsArchiveCreateRepairTaskIdErrorComponent
                | ApiV1RegionsArchiveCreateRepairTaskMetaErrorComponent
                | ApiV1RegionsArchiveCreateScopeErrorComponent
                | ApiV1RegionsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1RegionsArchiveCreateSlaTargetErrorComponent
                | ApiV1RegionsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1RegionsArchiveCreateSloTargetErrorComponent
                | ApiV1RegionsArchiveCreateStateErrorComponent
                | ApiV1RegionsArchiveCreateStateReasonErrorComponent
                | ApiV1RegionsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1RegionsArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_0 = (
                        ApiV1RegionsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_1 = (
                        ApiV1RegionsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_2 = (
                        ApiV1RegionsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_3 = (
                        ApiV1RegionsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_4 = (
                        ApiV1RegionsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_5 = (
                        ApiV1RegionsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_6 = (
                        ApiV1RegionsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_7 = (
                        ApiV1RegionsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_8 = (
                        ApiV1RegionsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_9 = (
                        ApiV1RegionsArchiveCreateStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_10 = (
                        ApiV1RegionsArchiveCreateStateReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_11 = (
                        ApiV1RegionsArchiveCreateLastStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_12 = (
                        ApiV1RegionsArchiveCreateLastStateChangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_13 = (
                        ApiV1RegionsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_14 = (
                        ApiV1RegionsArchiveCreateReconciliationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_15 = (
                        ApiV1RegionsArchiveCreateReconciliationTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_16 = (
                        ApiV1RegionsArchiveCreateReconciliationTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_17 = (
                        ApiV1RegionsArchiveCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_18 = (
                        ApiV1RegionsArchiveCreateDiscoveryRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_19 = (
                        ApiV1RegionsArchiveCreateDiscoveryTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_20 = (
                        ApiV1RegionsArchiveCreateDiscoveryTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_21 = (
                        ApiV1RegionsArchiveCreateRepairRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_22 = (
                        ApiV1RegionsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_23 = (
                        ApiV1RegionsArchiveCreateRepairTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_24 = (
                        ApiV1RegionsArchiveCreateRepairTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_25 = (
                        ApiV1RegionsArchiveCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_26 = (
                        ApiV1RegionsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_27 = (
                        ApiV1RegionsArchiveCreateConditionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_28 = (
                        ApiV1RegionsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_29 = (
                        ApiV1RegionsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_30 = (
                        ApiV1RegionsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_31 = (
                        ApiV1RegionsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_32 = (
                        ApiV1RegionsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_33 = (
                        ApiV1RegionsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_34 = (
                        ApiV1RegionsArchiveCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_35 = (
                        ApiV1RegionsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_36 = (
                        ApiV1RegionsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_37 = (
                        ApiV1RegionsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_38 = (
                        ApiV1RegionsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_39 = (
                        ApiV1RegionsArchiveCreatePlatformFeaturesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_archive_create_error_type_40 = (
                        ApiV1RegionsArchiveCreatePlatformFeaturesINDEXErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_archive_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_regions_archive_create_error_type_41 = (
                    ApiV1RegionsArchiveCreateConfigErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_regions_archive_create_error_type_41

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_regions_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_regions_archive_create_validation_error.additional_properties = d
        return api_v1_regions_archive_create_validation_error

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
