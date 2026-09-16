from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_worker_pools_partial_update_actual_availability_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_annotations_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_archived_at_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_archived_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_archived_reason_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_controlplane_id_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateControlplaneIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_criticality_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_debug_mode_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_desired_count_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateDesiredCountErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_discovery_enabled_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_display_name_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_hardening_enabled_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateHardeningEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_image_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateImageErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_kind_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_labels_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_location_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateLocationErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_name_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_non_field_errors_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_platform_service_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_product_id_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateProductIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_provider_account_id_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateProviderAccountIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_provider_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_provider_id_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_provider_reference_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_reconciliation_enabled_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_scope_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_sla_availability_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_sla_target_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_slo_availability_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_slo_target_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_ssh_key_credential_id_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateSshKeyCredentialIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_worker_pools_partial_update_target_availability_error_component import (
        ApiV1KubernetesWorkerPoolsPartialUpdateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesWorkerPoolsPartialUpdateValidationError")


@_attrs_define
class ApiV1KubernetesWorkerPoolsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesWorkerPoolsPartialUpdateActualAvailabilityErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateAnnotationsErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateArchivedAtErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateArchivedErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateArchivedReasonErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateControlplaneIdErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateCriticalityErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateDebugModeErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateDesiredCountErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateDisplayNameErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateHardeningEnabledErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateImageErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateKindErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateLabelsErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateLocationErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateNameErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdatePlatformServiceErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateProductIdErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateProviderAccountIdErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateProviderErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateProviderIdErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateProviderReferenceErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateScopeErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateSlaTargetErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateSloTargetErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateSshKeyCredentialIdErrorComponent |
            ApiV1KubernetesWorkerPoolsPartialUpdateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesWorkerPoolsPartialUpdateActualAvailabilityErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateAnnotationsErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateArchivedAtErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateArchivedErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateArchivedReasonErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateControlplaneIdErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateCriticalityErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateDebugModeErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateDesiredCountErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateDisplayNameErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateHardeningEnabledErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateImageErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateKindErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateLabelsErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateLocationErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateNameErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdatePlatformServiceErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateProductIdErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateProviderAccountIdErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateProviderErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateProviderIdErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateProviderReferenceErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateScopeErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateSlaTargetErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateSloTargetErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateSshKeyCredentialIdErrorComponent
        | ApiV1KubernetesWorkerPoolsPartialUpdateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_worker_pools_partial_update_actual_availability_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_annotations_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_archived_at_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_archived_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_archived_reason_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_controlplane_id_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateControlplaneIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_criticality_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_debug_mode_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_desired_count_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateDesiredCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_discovery_enabled_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_display_name_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_image_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateImageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_kind_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_labels_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_location_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateLocationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_name_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_non_field_errors_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_platform_service_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_product_id_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateProductIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_provider_account_id_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateProviderAccountIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_provider_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_provider_id_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_provider_reference_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_scope_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_sla_availability_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_sla_target_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_slo_availability_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_slo_target_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_ssh_key_credential_id_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateSshKeyCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_target_availability_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateControlplaneIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateProviderAccountIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateProductIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateDesiredCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateImageErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateLocationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesWorkerPoolsPartialUpdateSshKeyCredentialIdErrorComponent):
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
        from ..models.api_v1_kubernetes_worker_pools_partial_update_actual_availability_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_annotations_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_archived_at_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_archived_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_archived_reason_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_controlplane_id_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateControlplaneIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_criticality_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_debug_mode_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_desired_count_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateDesiredCountErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_discovery_enabled_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_display_name_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_hardening_enabled_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateHardeningEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_image_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateImageErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_kind_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_labels_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_location_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateLocationErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_name_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_non_field_errors_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_platform_service_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_product_id_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateProductIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_provider_account_id_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateProviderAccountIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_provider_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_provider_id_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_provider_reference_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_scope_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_sla_availability_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_sla_target_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_slo_availability_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_slo_target_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_ssh_key_credential_id_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateSshKeyCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_worker_pools_partial_update_target_availability_error_component import (
            ApiV1KubernetesWorkerPoolsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesWorkerPoolsPartialUpdateActualAvailabilityErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateAnnotationsErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateArchivedAtErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateArchivedErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateArchivedReasonErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateControlplaneIdErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateCriticalityErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateDebugModeErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateDesiredCountErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateDisplayNameErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateHardeningEnabledErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateImageErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateKindErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateLabelsErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateLocationErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateNameErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdatePlatformServiceErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateProductIdErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateProviderAccountIdErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateProviderErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateProviderIdErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateProviderReferenceErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateScopeErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateSlaTargetErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateSloTargetErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateSshKeyCredentialIdErrorComponent
                | ApiV1KubernetesWorkerPoolsPartialUpdateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_0 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_1 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_2 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_3 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_4 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_5 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_6 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_7 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_8 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_9 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_10 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_11 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_12 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_13 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_14 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_15 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_16 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_17 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_18 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_19 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_20 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_21 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_22 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_23 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_24 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateControlplaneIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_25 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateProviderAccountIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_26 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateProductIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_27 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateDesiredCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_28 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateImageErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_29 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateLocationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_30 = (
                        ApiV1KubernetesWorkerPoolsPartialUpdateSshKeyCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_31 = (
                    ApiV1KubernetesWorkerPoolsPartialUpdateHardeningEnabledErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_worker_pools_partial_update_error_type_31

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_worker_pools_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_worker_pools_partial_update_validation_error.additional_properties = d
        return api_v1_kubernetes_worker_pools_partial_update_validation_error

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
