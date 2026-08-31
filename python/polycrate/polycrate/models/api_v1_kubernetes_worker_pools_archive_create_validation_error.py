from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_worker_pools_archive_create_actual_availability_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_annotations_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_archived_at_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_archived_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_archived_reason_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_controlplane_id_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateControlplaneIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_criticality_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_debug_mode_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_desired_count_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateDesiredCountErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_discovery_enabled_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_display_name_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_hardening_enabled_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateHardeningEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_image_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateImageErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_kind_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_labels_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_location_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateLocationErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_name_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_non_field_errors_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_platform_service_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_product_id_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateProductIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_provider_account_id_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateProviderAccountIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_provider_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_provider_id_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_provider_reference_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_scope_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_sla_availability_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_sla_target_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_slo_availability_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_slo_target_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_ssh_key_credential_id_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateSshKeyCredentialIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_archive_create_target_availability_error_component import (
        ApiV1KubernetesWorkerPoolsArchiveCreateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesWorkerPoolsArchiveCreateValidationError")


@_attrs_define
class ApiV1KubernetesWorkerPoolsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesWorkerPoolsArchiveCreateActualAvailabilityErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateAnnotationsErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateArchivedAtErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateArchivedErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateArchivedReasonErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateControlplaneIdErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateCriticalityErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateDebugModeErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateDesiredCountErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateDisplayNameErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateHardeningEnabledErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateImageErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateKindErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateLabelsErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateLocationErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateNameErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreatePlatformServiceErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateProductIdErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateProviderAccountIdErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateProviderErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateProviderIdErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateProviderReferenceErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateScopeErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateSlaTargetErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateSloTargetErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateSshKeyCredentialIdErrorComponent |
            ApiV1KubernetesWorkerPoolsArchiveCreateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesWorkerPoolsArchiveCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateAnnotationsErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateArchivedAtErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateArchivedErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateArchivedReasonErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateControlplaneIdErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateCriticalityErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateDebugModeErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateDesiredCountErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateDisplayNameErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateHardeningEnabledErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateImageErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateKindErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateLabelsErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateLocationErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateNameErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreatePlatformServiceErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateProductIdErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateProviderAccountIdErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateProviderErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateProviderIdErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateProviderReferenceErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateScopeErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateSlaTargetErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateSloTargetErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateSshKeyCredentialIdErrorComponent
        | ApiV1KubernetesWorkerPoolsArchiveCreateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_worker_pools_archive_create_actual_availability_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_annotations_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_archived_at_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_archived_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_archived_reason_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_controlplane_id_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateControlplaneIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_criticality_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_debug_mode_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_desired_count_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateDesiredCountErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_discovery_enabled_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_display_name_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_image_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateImageErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_kind_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_labels_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_location_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateLocationErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_name_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_non_field_errors_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_platform_service_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_product_id_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateProductIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_provider_account_id_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateProviderAccountIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_provider_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_provider_id_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_provider_reference_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_scope_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_sla_availability_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_sla_target_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_slo_availability_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_slo_target_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_ssh_key_credential_id_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateSshKeyCredentialIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_target_availability_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateTargetAvailabilityErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateControlplaneIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateProviderAccountIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateProductIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateDesiredCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateImageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateLocationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsArchiveCreateSshKeyCredentialIdErrorComponent):
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
        from ..models.api_v1_kubernetes_worker_pools_archive_create_actual_availability_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_annotations_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_archived_at_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_archived_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_archived_reason_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_controlplane_id_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateControlplaneIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_criticality_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_debug_mode_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_desired_count_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateDesiredCountErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_discovery_enabled_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_display_name_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_hardening_enabled_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateHardeningEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_image_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateImageErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_kind_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_labels_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_location_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateLocationErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_name_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_non_field_errors_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_platform_service_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_product_id_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateProductIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_provider_account_id_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateProviderAccountIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_provider_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_provider_id_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_provider_reference_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_scope_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_sla_availability_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_sla_target_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_slo_availability_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_slo_target_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_ssh_key_credential_id_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateSshKeyCredentialIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_worker_pools_archive_create_target_availability_error_component import (
            ApiV1KubernetesWorkerPoolsArchiveCreateTargetAvailabilityErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesWorkerPoolsArchiveCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateAnnotationsErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateArchivedAtErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateArchivedErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateArchivedReasonErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateControlplaneIdErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateCriticalityErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateDebugModeErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateDesiredCountErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateDisplayNameErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateHardeningEnabledErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateImageErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateKindErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateLabelsErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateLocationErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateNameErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreatePlatformServiceErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateProductIdErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateProviderAccountIdErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateProviderErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateProviderIdErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateProviderReferenceErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateScopeErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateSlaTargetErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateSloTargetErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateSshKeyCredentialIdErrorComponent
                | ApiV1KubernetesWorkerPoolsArchiveCreateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_0 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_1 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_2 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_3 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_4 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_5 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_6 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_7 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_8 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_9 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_10 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_11 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_12 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_13 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_14 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_15 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_16 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_17 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_18 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_19 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_20 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_21 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_22 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_23 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_24 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateControlplaneIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_25 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateProviderAccountIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_26 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateProductIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_27 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateDesiredCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_28 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateImageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_29 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateLocationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_30 = (
                        ApiV1KubernetesWorkerPoolsArchiveCreateSshKeyCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_31 = (
                    ApiV1KubernetesWorkerPoolsArchiveCreateHardeningEnabledErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_worker_pools_archive_create_error_type_31

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_worker_pools_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_worker_pools_archive_create_validation_error.additional_properties = d
        return api_v1_kubernetes_worker_pools_archive_create_validation_error

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
