from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_policies_partial_update_annotations_error_component import (
        ApiV1PoliciesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_archived_at_error_component import (
        ApiV1PoliciesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_archived_error_component import (
        ApiV1PoliciesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_archived_reason_error_component import (
        ApiV1PoliciesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_criticality_error_component import (
        ApiV1PoliciesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_debug_mode_error_component import (
        ApiV1PoliciesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_description_error_component import (
        ApiV1PoliciesPartialUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_display_name_error_component import (
        ApiV1PoliciesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_expression_error_component import (
        ApiV1PoliciesPartialUpdateExpressionErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_kind_error_component import (
        ApiV1PoliciesPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_kinds_selector_error_component import (
        ApiV1PoliciesPartialUpdateKindsSelectorErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_labels_error_component import (
        ApiV1PoliciesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_metadata_error_component import (
        ApiV1PoliciesPartialUpdateMetadataErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_models_selector_error_component import (
        ApiV1PoliciesPartialUpdateModelsSelectorErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_name_error_component import (
        ApiV1PoliciesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_non_field_errors_error_component import (
        ApiV1PoliciesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_order_error_component import (
        ApiV1PoliciesPartialUpdateOrderErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_organizations_selector_error_component import (
        ApiV1PoliciesPartialUpdateOrganizationsSelectorErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_platform_service_error_component import (
        ApiV1PoliciesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_provider_error_component import (
        ApiV1PoliciesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_provider_id_error_component import (
        ApiV1PoliciesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_provider_reference_error_component import (
        ApiV1PoliciesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_reconciliation_enabled_error_component import (
        ApiV1PoliciesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_sla_availability_error_component import (
        ApiV1PoliciesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_sla_target_error_component import (
        ApiV1PoliciesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_slo_availability_error_component import (
        ApiV1PoliciesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_slo_target_error_component import (
        ApiV1PoliciesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_target_availability_error_component import (
        ApiV1PoliciesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_tolerations_error_component import (
        ApiV1PoliciesPartialUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_policies_partial_update_workspaces_selector_error_component import (
        ApiV1PoliciesPartialUpdateWorkspacesSelectorErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PoliciesPartialUpdateValidationError")


@_attrs_define
class ApiV1PoliciesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PoliciesPartialUpdateAnnotationsErrorComponent |
            ApiV1PoliciesPartialUpdateArchivedAtErrorComponent | ApiV1PoliciesPartialUpdateArchivedErrorComponent |
            ApiV1PoliciesPartialUpdateArchivedReasonErrorComponent | ApiV1PoliciesPartialUpdateCriticalityErrorComponent |
            ApiV1PoliciesPartialUpdateDebugModeErrorComponent | ApiV1PoliciesPartialUpdateDescriptionErrorComponent |
            ApiV1PoliciesPartialUpdateDisplayNameErrorComponent | ApiV1PoliciesPartialUpdateExpressionErrorComponent |
            ApiV1PoliciesPartialUpdateKindErrorComponent | ApiV1PoliciesPartialUpdateKindsSelectorErrorComponent |
            ApiV1PoliciesPartialUpdateLabelsErrorComponent | ApiV1PoliciesPartialUpdateMetadataErrorComponent |
            ApiV1PoliciesPartialUpdateModelsSelectorErrorComponent | ApiV1PoliciesPartialUpdateNameErrorComponent |
            ApiV1PoliciesPartialUpdateNonFieldErrorsErrorComponent | ApiV1PoliciesPartialUpdateOrderErrorComponent |
            ApiV1PoliciesPartialUpdateOrganizationsSelectorErrorComponent |
            ApiV1PoliciesPartialUpdatePlatformServiceErrorComponent | ApiV1PoliciesPartialUpdateProviderErrorComponent |
            ApiV1PoliciesPartialUpdateProviderIdErrorComponent | ApiV1PoliciesPartialUpdateProviderReferenceErrorComponent |
            ApiV1PoliciesPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1PoliciesPartialUpdateSlaAvailabilityErrorComponent | ApiV1PoliciesPartialUpdateSlaTargetErrorComponent |
            ApiV1PoliciesPartialUpdateSloAvailabilityErrorComponent | ApiV1PoliciesPartialUpdateSloTargetErrorComponent |
            ApiV1PoliciesPartialUpdateTargetAvailabilityErrorComponent | ApiV1PoliciesPartialUpdateTolerationsErrorComponent
            | ApiV1PoliciesPartialUpdateWorkspacesSelectorErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PoliciesPartialUpdateAnnotationsErrorComponent
        | ApiV1PoliciesPartialUpdateArchivedAtErrorComponent
        | ApiV1PoliciesPartialUpdateArchivedErrorComponent
        | ApiV1PoliciesPartialUpdateArchivedReasonErrorComponent
        | ApiV1PoliciesPartialUpdateCriticalityErrorComponent
        | ApiV1PoliciesPartialUpdateDebugModeErrorComponent
        | ApiV1PoliciesPartialUpdateDescriptionErrorComponent
        | ApiV1PoliciesPartialUpdateDisplayNameErrorComponent
        | ApiV1PoliciesPartialUpdateExpressionErrorComponent
        | ApiV1PoliciesPartialUpdateKindErrorComponent
        | ApiV1PoliciesPartialUpdateKindsSelectorErrorComponent
        | ApiV1PoliciesPartialUpdateLabelsErrorComponent
        | ApiV1PoliciesPartialUpdateMetadataErrorComponent
        | ApiV1PoliciesPartialUpdateModelsSelectorErrorComponent
        | ApiV1PoliciesPartialUpdateNameErrorComponent
        | ApiV1PoliciesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1PoliciesPartialUpdateOrderErrorComponent
        | ApiV1PoliciesPartialUpdateOrganizationsSelectorErrorComponent
        | ApiV1PoliciesPartialUpdatePlatformServiceErrorComponent
        | ApiV1PoliciesPartialUpdateProviderErrorComponent
        | ApiV1PoliciesPartialUpdateProviderIdErrorComponent
        | ApiV1PoliciesPartialUpdateProviderReferenceErrorComponent
        | ApiV1PoliciesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1PoliciesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1PoliciesPartialUpdateSlaTargetErrorComponent
        | ApiV1PoliciesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1PoliciesPartialUpdateSloTargetErrorComponent
        | ApiV1PoliciesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1PoliciesPartialUpdateTolerationsErrorComponent
        | ApiV1PoliciesPartialUpdateWorkspacesSelectorErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_policies_partial_update_annotations_error_component import (
            ApiV1PoliciesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_archived_at_error_component import (
            ApiV1PoliciesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_archived_error_component import (
            ApiV1PoliciesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_archived_reason_error_component import (
            ApiV1PoliciesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_criticality_error_component import (
            ApiV1PoliciesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_debug_mode_error_component import (
            ApiV1PoliciesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_description_error_component import (
            ApiV1PoliciesPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_display_name_error_component import (
            ApiV1PoliciesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_expression_error_component import (
            ApiV1PoliciesPartialUpdateExpressionErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_kind_error_component import (
            ApiV1PoliciesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_kinds_selector_error_component import (
            ApiV1PoliciesPartialUpdateKindsSelectorErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_labels_error_component import (
            ApiV1PoliciesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_models_selector_error_component import (
            ApiV1PoliciesPartialUpdateModelsSelectorErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_name_error_component import (
            ApiV1PoliciesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_non_field_errors_error_component import (
            ApiV1PoliciesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_order_error_component import (
            ApiV1PoliciesPartialUpdateOrderErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_organizations_selector_error_component import (
            ApiV1PoliciesPartialUpdateOrganizationsSelectorErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_platform_service_error_component import (
            ApiV1PoliciesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_provider_error_component import (
            ApiV1PoliciesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_provider_id_error_component import (
            ApiV1PoliciesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_provider_reference_error_component import (
            ApiV1PoliciesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_reconciliation_enabled_error_component import (
            ApiV1PoliciesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_sla_availability_error_component import (
            ApiV1PoliciesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_sla_target_error_component import (
            ApiV1PoliciesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_slo_availability_error_component import (
            ApiV1PoliciesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_slo_target_error_component import (
            ApiV1PoliciesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_target_availability_error_component import (
            ApiV1PoliciesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_tolerations_error_component import (
            ApiV1PoliciesPartialUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_workspaces_selector_error_component import (
            ApiV1PoliciesPartialUpdateWorkspacesSelectorErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PoliciesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateExpressionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateOrderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateModelsSelectorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateOrganizationsSelectorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateWorkspacesSelectorErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PoliciesPartialUpdateKindsSelectorErrorComponent):
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
        from ..models.api_v1_policies_partial_update_annotations_error_component import (
            ApiV1PoliciesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_archived_at_error_component import (
            ApiV1PoliciesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_archived_error_component import (
            ApiV1PoliciesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_archived_reason_error_component import (
            ApiV1PoliciesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_criticality_error_component import (
            ApiV1PoliciesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_debug_mode_error_component import (
            ApiV1PoliciesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_description_error_component import (
            ApiV1PoliciesPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_display_name_error_component import (
            ApiV1PoliciesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_expression_error_component import (
            ApiV1PoliciesPartialUpdateExpressionErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_kind_error_component import (
            ApiV1PoliciesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_kinds_selector_error_component import (
            ApiV1PoliciesPartialUpdateKindsSelectorErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_labels_error_component import (
            ApiV1PoliciesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_metadata_error_component import (
            ApiV1PoliciesPartialUpdateMetadataErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_models_selector_error_component import (
            ApiV1PoliciesPartialUpdateModelsSelectorErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_name_error_component import (
            ApiV1PoliciesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_non_field_errors_error_component import (
            ApiV1PoliciesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_order_error_component import (
            ApiV1PoliciesPartialUpdateOrderErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_organizations_selector_error_component import (
            ApiV1PoliciesPartialUpdateOrganizationsSelectorErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_platform_service_error_component import (
            ApiV1PoliciesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_provider_error_component import (
            ApiV1PoliciesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_provider_id_error_component import (
            ApiV1PoliciesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_provider_reference_error_component import (
            ApiV1PoliciesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_reconciliation_enabled_error_component import (
            ApiV1PoliciesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_sla_availability_error_component import (
            ApiV1PoliciesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_sla_target_error_component import (
            ApiV1PoliciesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_slo_availability_error_component import (
            ApiV1PoliciesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_slo_target_error_component import (
            ApiV1PoliciesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_target_availability_error_component import (
            ApiV1PoliciesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_tolerations_error_component import (
            ApiV1PoliciesPartialUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_policies_partial_update_workspaces_selector_error_component import (
            ApiV1PoliciesPartialUpdateWorkspacesSelectorErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PoliciesPartialUpdateAnnotationsErrorComponent
                | ApiV1PoliciesPartialUpdateArchivedAtErrorComponent
                | ApiV1PoliciesPartialUpdateArchivedErrorComponent
                | ApiV1PoliciesPartialUpdateArchivedReasonErrorComponent
                | ApiV1PoliciesPartialUpdateCriticalityErrorComponent
                | ApiV1PoliciesPartialUpdateDebugModeErrorComponent
                | ApiV1PoliciesPartialUpdateDescriptionErrorComponent
                | ApiV1PoliciesPartialUpdateDisplayNameErrorComponent
                | ApiV1PoliciesPartialUpdateExpressionErrorComponent
                | ApiV1PoliciesPartialUpdateKindErrorComponent
                | ApiV1PoliciesPartialUpdateKindsSelectorErrorComponent
                | ApiV1PoliciesPartialUpdateLabelsErrorComponent
                | ApiV1PoliciesPartialUpdateMetadataErrorComponent
                | ApiV1PoliciesPartialUpdateModelsSelectorErrorComponent
                | ApiV1PoliciesPartialUpdateNameErrorComponent
                | ApiV1PoliciesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1PoliciesPartialUpdateOrderErrorComponent
                | ApiV1PoliciesPartialUpdateOrganizationsSelectorErrorComponent
                | ApiV1PoliciesPartialUpdatePlatformServiceErrorComponent
                | ApiV1PoliciesPartialUpdateProviderErrorComponent
                | ApiV1PoliciesPartialUpdateProviderIdErrorComponent
                | ApiV1PoliciesPartialUpdateProviderReferenceErrorComponent
                | ApiV1PoliciesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1PoliciesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1PoliciesPartialUpdateSlaTargetErrorComponent
                | ApiV1PoliciesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1PoliciesPartialUpdateSloTargetErrorComponent
                | ApiV1PoliciesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1PoliciesPartialUpdateTolerationsErrorComponent
                | ApiV1PoliciesPartialUpdateWorkspacesSelectorErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_0 = (
                        ApiV1PoliciesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_1 = (
                        ApiV1PoliciesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_2 = (
                        ApiV1PoliciesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_3 = (
                        ApiV1PoliciesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_4 = (
                        ApiV1PoliciesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_5 = (
                        ApiV1PoliciesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_6 = (
                        ApiV1PoliciesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_7 = (
                        ApiV1PoliciesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_8 = (
                        ApiV1PoliciesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_9 = (
                        ApiV1PoliciesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_10 = (
                        ApiV1PoliciesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_11 = (
                        ApiV1PoliciesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_12 = (
                        ApiV1PoliciesPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_13 = (
                        ApiV1PoliciesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_14 = (
                        ApiV1PoliciesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_15 = (
                        ApiV1PoliciesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_16 = (
                        ApiV1PoliciesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_17 = (
                        ApiV1PoliciesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_18 = (
                        ApiV1PoliciesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_19 = (
                        ApiV1PoliciesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_20 = (
                        ApiV1PoliciesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_21 = (
                        ApiV1PoliciesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_22 = (
                        ApiV1PoliciesPartialUpdateExpressionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_23 = (
                        ApiV1PoliciesPartialUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_24 = (
                        ApiV1PoliciesPartialUpdateOrderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_25 = (
                        ApiV1PoliciesPartialUpdateModelsSelectorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_26 = (
                        ApiV1PoliciesPartialUpdateOrganizationsSelectorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_27 = (
                        ApiV1PoliciesPartialUpdateWorkspacesSelectorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_policies_partial_update_error_type_28 = (
                        ApiV1PoliciesPartialUpdateKindsSelectorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_policies_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_policies_partial_update_error_type_29 = (
                    ApiV1PoliciesPartialUpdateMetadataErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_policies_partial_update_error_type_29

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_policies_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_policies_partial_update_validation_error.additional_properties = d
        return api_v1_policies_partial_update_validation_error

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
