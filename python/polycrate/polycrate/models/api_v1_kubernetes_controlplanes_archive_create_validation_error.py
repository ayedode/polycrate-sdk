from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_controlplanes_archive_create_actual_availability_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_annotations_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_archived_at_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_archived_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_archived_reason_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_cluster_domain_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateClusterDomainErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_criticality_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_debug_mode_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_discovery_enabled_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_display_name_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_kind_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_labels_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_loadbalancer_mode_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateLoadbalancerModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_loadbalancer_provider_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateLoadbalancerProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_name_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_non_field_errors_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_persistence_size_error_component import (
        ApiV1KubernetesControlplanesArchiveCreatePersistenceSizeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_platform_service_error_component import (
        ApiV1KubernetesControlplanesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_provider_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_provider_id_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_provider_reference_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_scope_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_sla_availability_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_sla_target_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_slo_availability_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_slo_target_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_storage_class_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateStorageClassErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_archive_create_target_availability_error_component import (
        ApiV1KubernetesControlplanesArchiveCreateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesControlplanesArchiveCreateValidationError")


@_attrs_define
class ApiV1KubernetesControlplanesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesControlplanesArchiveCreateActualAvailabilityErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateAnnotationsErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateArchivedAtErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateArchivedErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateArchivedReasonErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateClusterDomainErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateCriticalityErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateDebugModeErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateDisplayNameErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateKindErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateLabelsErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateLoadbalancerModeErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateLoadbalancerProviderErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateNameErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreatePersistenceSizeErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreatePlatformServiceErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateProviderErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateProviderIdErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateProviderReferenceErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateScopeErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateSlaTargetErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateSloTargetErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateStorageClassErrorComponent |
            ApiV1KubernetesControlplanesArchiveCreateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesControlplanesArchiveCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateAnnotationsErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateArchivedAtErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateArchivedErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateArchivedReasonErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateClusterDomainErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateCriticalityErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateDebugModeErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateDisplayNameErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateKindErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateLabelsErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateLoadbalancerModeErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateLoadbalancerProviderErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateNameErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreatePersistenceSizeErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreatePlatformServiceErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateProviderErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateProviderIdErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateProviderReferenceErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateScopeErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateSlaTargetErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateSloTargetErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateStorageClassErrorComponent
        | ApiV1KubernetesControlplanesArchiveCreateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_controlplanes_archive_create_actual_availability_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_annotations_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_archived_at_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_archived_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_archived_reason_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_criticality_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_debug_mode_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_discovery_enabled_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_display_name_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_kind_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_labels_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_loadbalancer_mode_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateLoadbalancerModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_loadbalancer_provider_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateLoadbalancerProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_name_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_non_field_errors_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_persistence_size_error_component import (
            ApiV1KubernetesControlplanesArchiveCreatePersistenceSizeErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_platform_service_error_component import (
            ApiV1KubernetesControlplanesArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_provider_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_provider_id_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_provider_reference_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_scope_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_sla_availability_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_sla_target_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_slo_availability_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_slo_target_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_storage_class_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateStorageClassErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_target_availability_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateTargetAvailabilityErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesControlplanesArchiveCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesControlplanesArchiveCreateTargetAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesControlplanesArchiveCreateActualAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreateLoadbalancerModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesControlplanesArchiveCreateLoadbalancerProviderErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreateStorageClassErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesArchiveCreatePersistenceSizeErrorComponent):
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
        from ..models.api_v1_kubernetes_controlplanes_archive_create_actual_availability_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_annotations_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_archived_at_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_archived_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_archived_reason_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_cluster_domain_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateClusterDomainErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_criticality_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_debug_mode_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_discovery_enabled_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_display_name_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_kind_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_labels_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_loadbalancer_mode_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateLoadbalancerModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_loadbalancer_provider_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateLoadbalancerProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_name_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_non_field_errors_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_persistence_size_error_component import (
            ApiV1KubernetesControlplanesArchiveCreatePersistenceSizeErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_platform_service_error_component import (
            ApiV1KubernetesControlplanesArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_provider_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_provider_id_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_provider_reference_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_scope_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_sla_availability_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_sla_target_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_slo_availability_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_slo_target_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_storage_class_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateStorageClassErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_archive_create_target_availability_error_component import (
            ApiV1KubernetesControlplanesArchiveCreateTargetAvailabilityErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesControlplanesArchiveCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateAnnotationsErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateArchivedAtErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateArchivedErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateArchivedReasonErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateClusterDomainErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateCriticalityErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateDebugModeErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateDisplayNameErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateKindErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateLabelsErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateLoadbalancerModeErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateLoadbalancerProviderErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateNameErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreatePersistenceSizeErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreatePlatformServiceErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateProviderErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateProviderIdErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateProviderReferenceErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateScopeErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateSlaTargetErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateSloTargetErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateStorageClassErrorComponent
                | ApiV1KubernetesControlplanesArchiveCreateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_0 = (
                        ApiV1KubernetesControlplanesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_1 = (
                        ApiV1KubernetesControlplanesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_2 = (
                        ApiV1KubernetesControlplanesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_3 = (
                        ApiV1KubernetesControlplanesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_4 = (
                        ApiV1KubernetesControlplanesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_5 = (
                        ApiV1KubernetesControlplanesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_6 = (
                        ApiV1KubernetesControlplanesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_7 = (
                        ApiV1KubernetesControlplanesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_8 = (
                        ApiV1KubernetesControlplanesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_9 = (
                        ApiV1KubernetesControlplanesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_10 = (
                        ApiV1KubernetesControlplanesArchiveCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_11 = (
                        ApiV1KubernetesControlplanesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_12 = (
                        ApiV1KubernetesControlplanesArchiveCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_13 = (
                        ApiV1KubernetesControlplanesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_14 = (
                        ApiV1KubernetesControlplanesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_15 = (
                        ApiV1KubernetesControlplanesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_16 = (
                        ApiV1KubernetesControlplanesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_17 = (
                        ApiV1KubernetesControlplanesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_18 = (
                        ApiV1KubernetesControlplanesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_19 = (
                        ApiV1KubernetesControlplanesArchiveCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_20 = (
                        ApiV1KubernetesControlplanesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_21 = (
                        ApiV1KubernetesControlplanesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_22 = (
                        ApiV1KubernetesControlplanesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_23 = (
                        ApiV1KubernetesControlplanesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_24 = (
                        ApiV1KubernetesControlplanesArchiveCreateLoadbalancerModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_25 = (
                        ApiV1KubernetesControlplanesArchiveCreateLoadbalancerProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_26 = (
                        ApiV1KubernetesControlplanesArchiveCreateStorageClassErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_27 = (
                        ApiV1KubernetesControlplanesArchiveCreatePersistenceSizeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_28 = (
                    ApiV1KubernetesControlplanesArchiveCreateClusterDomainErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_controlplanes_archive_create_error_type_28

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_controlplanes_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_controlplanes_archive_create_validation_error.additional_properties = d
        return api_v1_kubernetes_controlplanes_archive_create_validation_error

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
